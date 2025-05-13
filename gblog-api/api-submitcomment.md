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

## POST submintComment

POST /comment

> Body 请求参数

```json
{
  "nickname": "string",
  "email": "string",
  "website": "string",
  "content": "string",
  "page": 0,
  "isNotice": true,
  "parentCommentId": 0,
  "blogId": 0
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|[CommentForm](#schemacommentform)| 否 |none|

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

<h2 id="tocS_Comment">Comment</h2>

<a id="schemacomment"></a>
<a id="schema_Comment"></a>
<a id="tocScomment"></a>
<a id="tocscomment"></a>

```json
{
  "id": 0,
  "nickname": "string",
  "email": "string",
  "qq": 0,
  "avatar": "string",
  "createTime": "string",
  "website": "string",
  "ip": "string",
  "content": "string",
  "isPublished": true,
  "adminComment": true,
  "page": 0,
  "isNotice": true,
  "parentCommentId": 0,
  "rootCommentId": "string",
  "blogId": 0
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|id|integer|true|none||none|
|nickname|string|true|none||none|
|email|string|true|none||none|
|qq|integer|true|none||none|
|avatar|string|true|none||none|
|createTime|string|true|none||none|
|website|string|true|none||none|
|ip|string|true|none||none|
|content|string|true|none||none|
|isPublished|boolean|true|none||none|
|adminComment|boolean|true|none||none|
|page|integer|true|none|所属页面|0为blog页面，1为about页面|
|isNotice|boolean|true|none||none|
|parentCommentId|integer|true|none||none|
|rootCommentId|string|true|none|所属顶级评论id|顶级评论为-1|
|blogId|integer|true|none||none|

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

<h2 id="tocS_CommentForm">CommentForm</h2>

<a id="schemacommentform"></a>
<a id="schema_CommentForm"></a>
<a id="tocScommentform"></a>
<a id="tocscommentform"></a>

```json
{
  "nickname": "string",
  "email": "string",
  "website": "string",
  "content": "string",
  "page": 0,
  "isNotice": true,
  "parentCommentId": 0,
  "blogId": 0
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|nickname|string|true|none||none|
|email|string|true|none||none|
|website|string|true|none||none|
|content|string|true|none||none|
|page|integer|true|none|所属页面|0为blog页面，1为about页面|
|isNotice|boolean|true|none||none|
|parentCommentId|integer|true|none||none|
|blogId|integer|true|none||none|

