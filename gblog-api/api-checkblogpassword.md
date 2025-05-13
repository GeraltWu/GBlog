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

## POST checkBlogPassword

POST /check-blog-password

> Body 请求参数

```json
{
  "blogId": 0,
  "password": "string"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|[BlogPasswordForm](#schemablogpasswordform)| 否 |none|

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
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Result](#schemaresult)|

# 数据模型

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

<h2 id="tocS_BlogPasswordForm">BlogPasswordForm</h2>

<a id="schemablogpasswordform"></a>
<a id="schema_BlogPasswordForm"></a>
<a id="tocSblogpasswordform"></a>
<a id="tocsblogpasswordform"></a>

```json
{
  "blogId": 0,
  "password": "string"
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|blogId|integer|true|none||none|
|password|string|true|none||none|

