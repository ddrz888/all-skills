---
name: elysia-framework-patterns
description: Comprehensive guide for building high-performance, type-safe web applications with ElysiaJS framework. Covers plugin architecture, schema validation, lifecycle hooks, authentication patterns, database integration, and Bun runtime optimization. Use when building REST APIs, microservices, or backend applications with ElysiaJS, implementing authentication systems, setting up validation schemas, creating modular plugin-based architectures, or optimizing performance with Bun runtime.
---

# ElysiaJS Framework Patterns

## Overview

ElysiaJS is an ergonomic and highly performant web framework for TypeScript, supercharged by Bun. This skill provides comprehensive patterns and best practices for building production-ready applications with end-to-end type safety.

## Core Concepts

### Type Safety & Schema Validation

ElysiaJS uses TypeBox for runtime validation with automatic TypeScript inference:

```typescript
import { Elysia, t } from 'elysia'

new Elysia()
  .post('/users', ({ body }) => body, {
    body: t.Object({
      name: t.String(),
      email: t.String({ format: 'email' }),
      age: t.Number({ minimum: 0, maximum: 120 })
    }),
    response: t.Object({
      id: t.Number(),
      name: t.String(),
      email: t.String()
    })
  })
  .listen(3000)
```

**Key Principles:**
- Validate all inputs (body, query, params, headers)
- Use response schemas for contract enforcement
- Leverage automatic type inference
- Create reusable model plugins for shared schemas

### Plugin Architecture

Plugins are the foundation of code organization in ElysiaJS:

```typescript
// auth.plugin.ts
import { Elysia } from 'elysia'

export const authPlugin = new Elysia({ name: 'auth' })
  .derive(({ headers }) => ({
    userId: headers['x-user-id']
  }))
  .guard({
    beforeHandle({ headers, error }) {
      if (!headers.authorization) {
        throw error(401, 'Unauthorized')
      }
    }
  })

// main.ts
import { Elysia } from 'elysia'
import { authPlugin } from './auth.plugin'

new Elysia()
  .use(authPlugin)
  .get('/protected', ({ userId }) => `User: ${userId}`)
  .listen(3000)
```

**Best Practices:**
- Name plugins for deduplication
- Use guards for scoped middleware
- Leverage derive for shared context
- Organize by feature/domain

### Lifecycle Hooks

Control request processing at specific stages:

```typescript
import { Elysia } from 'elysia'

new Elysia()
  .onBeforeHandle(({ request }) => {
    console.log(`[${new Date().toISOString()}] ${request.method} ${request.url}`)
  })
  .onAfterHandle(({ response }) => {
    console.log(`Response: ${response?.status}`)
  })
  .onError(({ error, code }) => {
    if (code === 'VALIDATION') {
      return { error: 'Invalid request', details: error }
    }
    return { error: 'Internal server error' }
  })
  .listen(3000)
```

**Available Hooks:**
- `onRequest` - Before request parsing
- `onBeforeHandle` - Before route handler
- `onAfterHandle` - After route handler
- `onError` - Error handling
- `onResponse` - After response sent

## Authentication Patterns

### JWT with HTTP-Only Cookies

```typescript
import { Elysia } from 'elysia'
import { jwt } from '@elysiajs/jwt'

const app = new Elysia()
  .use(jwt({
    name: 'jwt',
    secret: process.env.JWT_SECRET!
  }))
  
  .post('/sign-in', async ({ jwt, cookie: { auth }, body }) => {
    // Validate credentials
    const token = await jwt.sign({
      userId: body.userId,
      email: body.email
    })
    
    auth.set({
      value: token,
      httpOnly: true,
      maxAge: 7 * 86400,
      path: '/',
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'strict'
    })
    
    return { message: 'Signed in' }
  })
  
  .get('/profile', async ({ jwt, cookie: { auth }, error }) => {
    const profile = await jwt.verify(auth.value)
    if (!profile) throw error(401, 'Unauthorized')
    return profile
  })
  .listen(3000)
```

### Bearer Token Authentication

```typescript
import { Elysia } from 'elysia'
import { jwt } from '@elysiajs/jwt'

const app = new Elysia()
  .use(jwt({
    name: 'jwt',
    secret: process.env.JWT_SECRET!
  }))
  
  .post('/sign-in', async ({ jwt, body }) => {
    // Validate credentials
    const token = await jwt.sign({
      userId: body.userId,
      email: body.email
    })
    
    return { token }
  })
  
  .guard({
    async beforeHandle({ jwt, headers, error }) {
      const bearer = headers.authorization?.split(' ')[1]
      if (!bearer) throw error(401, 'Missing token')
      
      const profile = await jwt.verify(bearer)
      if (!profile) throw error(401, 'Invalid token')
    }
  }, (app) => app
    .get('/profile', ({ userId }) => ({ userId }))
    .get('/settings', () => 'User settings')
  )
  .listen(3000)
```

## Database Integration

### Drizzle ORM Setup

```typescript
import { Elysia } from 'elysia'
import { drizzle } from 'drizzle-orm/bun-sqlite'
import { Database } from 'bun:sqlite'
import { sqliteTable, text, integer } from 'drizzle-orm/sqlite-core'
import { eq } from 'drizzle-orm'

// Define schema
const users = sqliteTable('users', {
  id: integer('id').primaryKey(),
  name: text('name').notNull(),
  email: text('email').notNull().unique()
})

// Initialize database
const sqlite = new Database('app.db')
const db = drizzle(sqlite)

// Create plugin
const dbPlugin = new Elysia({ name: 'db' })
  .decorate('db', db)
  .decorate('schema', { users })

// Use in app
const app = new Elysia()
  .use(dbPlugin)
  
  .get('/users', async ({ db, schema }) => {
    return await db.select().from(schema.users)
  })
  
  .post('/users', async ({ db, schema, body }) => {
    const [user] = await db
      .insert(schema.users)
      .values(body)
      .returning()
    return user
  }, {
    body: t.Object({
      name: t.String(),
      email: t.String({ format: 'email' })
    })
  })
  
  .get('/users/:id', async ({ db, schema, params }) => {
    const [user] = await db
      .select()
      .from(schema.users)
      .where(eq(schema.users.id, params.id))
    return user
  })
  .listen(3000)
```

## Validation Patterns

### Multi-Level Validation

```typescript
import { Elysia, t } from 'elysia'

new Elysia()
  .get('/users/:id', ({ params, query, headers }) => {
    return {
      userId: params.id,
      page: query.page,
      token: headers.authorization
    }
  }, {
    params: t.Object({
      id: t.Number()
    }),
    query: t.Object({
      page: t.Number({ default: 1 }),
      limit: t.Number({ default: 10, maximum: 100 })
    }),
    headers: t.Object({
      authorization: t.String()
    }),
    response: t.Object({
      userId: t.Number(),
      page: t.Number(),
      token: t.String()
    })
  })
  .listen(3000)
```

### Reusable Model Plugin

```typescript
// models/user.model.ts
import { Elysia, t } from 'elysia'

export const userModel = new Elysia()
  .model({
    createUser: t.Object({
      name: t.String(),
      email: t.String({ format: 'email' }),
      password: t.String({ minLength: 8 })
    }),
    updateUser: t.Object({
      name: t.Optional(t.String()),
      email: t.Optional(t.String({ format: 'email' }))
    }),
    user: t.Object({
      id: t.Number(),
      name: t.String(),
      email: t.String(),
      createdAt: t.String()
    }),
    userList: t.Object({
      users: t.Array(t.Object({
        id: t.Number(),
        name: t.String(),
        email: t.String()
      })),
      total: t.Number(),
      page: t.Number()
    })
  })

// controllers/user.controller.ts
import { Elysia } from 'elysia'
import { userModel } from '../models/user.model'

export const userController = new Elysia({ prefix: '/users' })
  .use(userModel)
  
  .post('/', ({ body }) => body, {
    body: 'createUser',
    response: 'user'
  })
  
  .get('/', () => ({ users: [], total: 0, page: 1 }), {
    response: 'userList'
  })
```

## Error Handling

### Global Error Handler

```typescript
import { Elysia } from 'elysia'

class NotFoundError extends Error {
  constructor(message: string) {
    super(message)
    this.name = 'NotFoundError'
  }
}

class ValidationError extends Error {
  constructor(message: string) {
    super(message)
    this.name = 'ValidationError'
  }
}

const app = new Elysia()
  .onError(({ error, code }) => {
    console.error('[Error]', error)
    
    if (error instanceof NotFoundError) {
      return { error: error.message, status: 404 }
    }
    
    if (error instanceof ValidationError) {
      return { error: error.message, status: 400 }
    }
    
    if (code === 'NOT_FOUND') {
      return { error: 'Route not found', status: 404 }
    }
    
    if (code === 'VALIDATION') {
      return { 
        error: 'Validation failed', 
        details: error,
        status: 400 
      }
    }
    
    return { error: 'Internal server error', status: 500 }
  })
  .listen(3000)
```

### Local Error Handling

```typescript
import { Elysia } from 'elysia'

new Elysia()
  .get('/protected', () => 'Protected content', {
    beforeHandle({ headers, error }) {
      if (!headers.authorization) {
        throw error(401, 'Unauthorized')
      }
    },
    error({ code, error }) {
      if (code === 401) {
        return { error: 'Authentication required' }
      }
      return { error: error.message }
    }
  })
  .listen(3000)
```

## Project Structure

### Recommended Organization

```
src/
├── controllers/
│   ├── user.controller.ts
│   ├── auth.controller.ts
│   └── post.controller.ts
├── services/
│   ├── user.service.ts
│   ├── auth.service.ts
│   └── post.service.ts
├── models/
│   ├── user.model.ts
│   ├── auth.model.ts
│   └── post.model.ts
├── plugins/
│   ├── db.plugin.ts
│   ├── auth.plugin.ts
│   └── logger.plugin.ts
├── db/
│   ├── schema.ts
│   └── migrations/
├── config/
│   └── env.ts
└── index.ts
```

### Controller Pattern

```typescript
// controllers/user.controller.ts
import { Elysia, t } from 'elysia'
import { userModel } from '../models/user.model'
import { userService } from '../services/user.service'
import { authPlugin } from '../plugins/auth.plugin'

export const userController = new Elysia({ prefix: '/users' })
  .use(userModel)
  .use(authPlugin)
  
  .get('/', async () => {
    return await userService.findAll()
  }, {
    response: 'userList'
  })
  
  .get('/:id', async ({ params }) => {
    return await userService.findById(params.id)
  }, {
    params: t.Object({ id: t.Number() }),
    response: 'user'
  })
  
  .post('/', async ({ body }) => {
    return await userService.create(body)
  }, {
    body: 'createUser',
    response: 'user'
  })
  
  .patch('/:id', async ({ params, body }) => {
    return await userService.update(params.id, body)
  }, {
    params: t.Object({ id: t.Number() }),
    body: 'updateUser',
    response: 'user'
  })
  
  .delete('/:id', async ({ params }) => {
    await userService.delete(params.id)
    return { message: 'User deleted' }
  }, {
    params: t.Object({ id: t.Number() })
  })
```

### Service Layer

```typescript
// services/user.service.ts
import { db } from '../db'
import { users } from '../db/schema'
import { eq } from 'drizzle-orm'

export const userService = {
  async findAll() {
    return await db.select().from(users)
  },
  
  async findById(id: number) {
    const [user] = await db
      .select()
      .from(users)
      .where(eq(users.id, id))
    
    if (!user) {
      throw new NotFoundError('User not found')
    }
    
    return user
  },
  
  async create(data: typeof users.$inferInsert) {
    const [user] = await db
      .insert(users)
      .values(data)
      .returning()
    
    return user
  },
  
  async update(id: number, data: Partial<typeof users.$inferInsert>) {
    const [user] = await db
      .update(users)
      .set(data)
      .where(eq(users.id, id))
      .returning()
    
    if (!user) {
      throw new NotFoundError('User not found')
    }
    
    return user
  },
  
  async delete(id: number) {
    await db.delete(users).where(eq(users.id, id))
  }
}
```

## Performance Optimization

### Compression

```typescript
import { Elysia } from 'elysia'
import { compression } from 'elysia-compression'

new Elysia()
  .use(compression())
  .listen(3000)
```

### Response Caching

```typescript
import { Elysia } from 'elysia'

const cache = new Map<string, any>()

const cachePlugin = new Elysia({ name: 'cache' })
  .derive(({ request }) => ({
    cacheKey: `${request.method}:${request.url}`
  }))
  .macro({
    cache: (ttl: number) => ({
      beforeHandle({ cacheKey }) {
        const cached = cache.get(cacheKey)
        if (cached && Date.now() - cached.timestamp < ttl) {
          return cached.data
        }
      },
      afterHandle({ response, cacheKey }) {
        cache.set(cacheKey, {
          data: response,
          timestamp: Date.now()
        })
      }
    })
  })

new Elysia()
  .use(cachePlugin)
  .get('/data', () => expensiveOperation(), {
    cache: 60000 // Cache for 60 seconds
  })
  .listen(3000)
```

## Testing

### Basic Test Setup

```typescript
import { describe, expect, it } from 'bun:test'
import { Elysia } from 'elysia'
import { userController } from './controllers/user.controller'

describe('User API', () => {
  const app = new Elysia().use(userController)
  
  it('should get user by id', async () => {
    const response = await app
      .handle(new Request('http://localhost/users/1'))
      .then(r => r.json())
    
    expect(response).toHaveProperty('id', 1)
    expect(response).toHaveProperty('name')
  })
  
  it('should create user', async () => {
    const response = await app
      .handle(new Request('http://localhost/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: 'John Doe',
          email: 'john@example.com'
        })
      }))
      .then(r => r.json())
    
    expect(response).toHaveProperty('id')
    expect(response.name).toBe('John Doe')
  })
  
  it('should validate request body', async () => {
    const response = await app
      .handle(new Request('http://localhost/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: 'John'
          // Missing email
        })
      }))
    
    expect(response.status).toBe(400)
  })
})
```

## OpenAPI Documentation

### Swagger Setup

```typescript
import { Elysia } from 'elysia'
import { swagger } from '@elysiajs/swagger'

new Elysia()
  .use(swagger({
    documentation: {
      info: {
        title: 'My API',
        version: '1.0.0',
        description: 'API documentation'
      },
      tags: [
        { name: 'Users', description: 'User management' },
        { name: 'Auth', description: 'Authentication' }
      ],
      components: {
        securitySchemes: {
          bearerAuth: {
            type: 'http',
            scheme: 'bearer',
            bearerFormat: 'JWT'
          }
        }
      }
    }
  }))
  
  .group('/api', {
    detail: {
      tags: ['Users'],
      security: [{ bearerAuth: [] }]
    }
  }, (app) => app
    .get('/users', () => 'List users')
    .post('/users', () => 'Create user')
  )
  .listen(3000)
```

## Best Practices Summary

1. **Type Safety**
   - Always define schemas for inputs and outputs
   - Use TypeBox for runtime validation
   - Leverage automatic type inference

2. **Architecture**
   - Organize code into plugins by feature
   - Use controller/service/model pattern
   - Keep business logic in services

3. **Security**
   - Validate all inputs
   - Use HTTP-only cookies for sessions
   - Implement proper CORS configuration
   - Set secure cookie attributes in production

4. **Error Handling**
   - Use global onError for consistency
   - Create custom error classes
   - Return appropriate status codes
   - Log errors for debugging

5. **Performance**
   - Enable compression
   - Implement caching where appropriate
   - Optimize database queries
   - Use connection pooling

6. **Testing**
   - Test all endpoints
   - Validate error cases
   - Use Bun's test runner
   - Maintain high coverage

## Common Pitfalls

1. **Missing Schema Validation** - Always validate inputs
2. **Improper Error Handling** - Implement both global and local handlers
3. **Plugin Naming** - Name plugins to prevent duplication
4. **Cookie Security** - Set httpOnly, secure, and sameSite attributes
5. **Response Validation** - Validate outputs to maintain contracts
6. **Lifecycle Hook Order** - Place onError before handlers it protects
7. **Database Connections** - Share connections via decorators
8. **Type Assertions** - Let TypeBox infer types automatically

## Quick Reference

### Essential Imports
```typescript
import { Elysia, t } from 'elysia'
import { jwt } from '@elysiajs/jwt'
import { cors } from '@elysiajs/cors'
import { swagger } from '@elysiajs/swagger'
```

### Common Patterns
- Plugin: `new Elysia({ name: 'plugin' })`
- Guard: `.guard({ beforeHandle }, (app) => app)`
- Decorator: `.decorate('name', value)`
- Derive: `.derive(({ context }) => ({ derived }))`
- Model: `.model({ name: schema })`

### Lifecycle Order
1. onRequest
2. onBeforeHandle
3. Route Handler
4. onAfterHandle
5. onError (if error)
6. onResponse

This skill provides the foundation for building production-ready ElysiaJS applications with proper architecture, type safety, and performance optimization.
