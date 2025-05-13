---
title: blog
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.30"

---

# blog

Base URLs:

# Authentication

# 前台

## POST 登录

POST /login

> Body 请求参数

```json
{
  "username": "string",
  "password": "string"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|[LoginForm](#schemaloginform)| 否 |none|

> 返回示例

> 200 Response

```json
{
  "code": 200,
  "msg": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none|响应码|none|
|» msg|string|true|none||none|
|» data|object|true|none||none|

# 数据模型

<h2 id="tocS_User">User</h2>

<a id="schemauser"></a>
<a id="schema_User"></a>
<a id="tocSuser"></a>
<a id="tocsuser"></a>

```json
{
  "id": 0,
  "username": "string",
  "password": "string",
  "nickname": "string",
  "avatar": "string",
  "email": "string",
  "createTime": "string",
  "updateTime": "string",
  "role": "string"
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|id|integer|true|none||none|
|username|string|true|none||none|
|password|string|true|none||none|
|nickname|string|true|none||none|
|avatar|string|true|none||none|
|email|string|true|none||none|
|createTime|string|true|none||none|
|updateTime|string|true|none||none|
|role|string|true|none||none|

<h2 id="tocS_Result">Result</h2>

<a id="schemaresult"></a>
<a id="schema_Result"></a>
<a id="tocSresult"></a>
<a id="tocsresult"></a>

```json
{
  "code": 200,
  "msg": "string",
  "data": {}
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|code|integer|true|none|响应码|none|
|msg|string|true|none||none|
|data|object|true|none||none|

<h2 id="tocS_LoginForm">LoginForm</h2>

<a id="schemaloginform"></a>
<a id="schema_LoginForm"></a>
<a id="tocSloginform"></a>
<a id="tocsloginform"></a>

```json
{
  "username": "string",
  "password": "string"
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|username|string|true|none||none|
|password|string|true|none||none|

