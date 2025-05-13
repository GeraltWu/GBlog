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

## GET getCommentListByQuery

GET /comments

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|page|query|integer| 否 |页面分类（0普通文章，1关于我...）|
|blogId|query|integer| 否 |page==0时，需要提供blogId|
|pageNum|query|integer| 否 |none|
|pageSize|query|integer| 否 |每一页的comment数|
|Authorization|header|string| 否 |none|

> 返回示例

> 200 Response

```json
{
  "code": 200,
  "msg": "string",
  "data": {
    "allComment": 0,
    "closeComment": 0,
    "comments": {
      "totalPage": 0,
      "list": [
        {
          "id": 0,
          "nickname": "string",
          "content": "string",
          "avatar": "string",
          "createTime": "string",
          "website": "string",
          "adminComment": true,
          "parentCommentId": "string",
          "parentCommentNickname": "string",
          "replyComments": [
            null
          ]
        }
      ]
    }
  }
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
|»» allComment|integer|true|none||none|
|»» closeComment|integer|true|none||none|
|»» comments|object|true|none||none|
|»»» totalPage|integer|true|none||none|
|»»» list|[[PageCommentVO](#schemapagecommentvo)]|true|none||none|
|»»»» id|integer|true|none||none|
|»»»» nickname|string|true|none||none|
|»»»» content|string|true|none||none|
|»»»» avatar|string|true|none||none|
|»»»» createTime|string|true|none||none|
|»»»» website|string|true|none||none|
|»»»» adminComment|boolean|true|none||none|
|»»»» parentCommentId|string|true|none||none|
|»»»» parentCommentNickname|string|true|none||none|
|»»»» replyComments|[[PageCommentVO](#schemapagecommentvo)]|true|none||none|
|»»»»» id|integer|true|none||none|
|»»»»» nickname|string|true|none||none|
|»»»»» content|string|true|none||none|
|»»»»» avatar|string|true|none||none|
|»»»»» createTime|string|true|none||none|
|»»»»» website|string|true|none||none|
|»»»»» adminComment|boolean|true|none||none|
|»»»»» parentCommentId|string|true|none||none|
|»»»»» parentCommentNickname|string|true|none||none|
|»»»»» replyComments|[[PageCommentVO](#schemapagecommentvo)]|true|none||none|

# 数据模型

<h2 id="tocS_PageResult">PageResult</h2>

<a id="schemapageresult"></a>
<a id="schema_PageResult"></a>
<a id="tocSpageresult"></a>
<a id="tocspageresult"></a>

```json
{
  "totalPage": 0,
  "list": [
    {}
  ]
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|totalPage|integer|true|none||none|
|list|[object]|true|none||none|

<h2 id="tocS_PageCommentVO">PageCommentVO</h2>

<a id="schemapagecommentvo"></a>
<a id="schema_PageCommentVO"></a>
<a id="tocSpagecommentvo"></a>
<a id="tocspagecommentvo"></a>

```json
{
  "id": 0,
  "nickname": "string",
  "content": "string",
  "avatar": "string",
  "createTime": "string",
  "website": "string",
  "adminComment": true,
  "parentCommentId": "string",
  "parentCommentNickname": "string",
  "replyComments": [
    {
      "id": 0,
      "nickname": "string",
      "content": "string",
      "avatar": "string",
      "createTime": "string",
      "website": "string",
      "adminComment": true,
      "parentCommentId": "string",
      "parentCommentNickname": "string",
      "replyComments": [
        {
          "id": 0,
          "nickname": "string",
          "content": "string",
          "avatar": "string",
          "createTime": "string",
          "website": "string",
          "adminComment": true,
          "parentCommentId": "string",
          "parentCommentNickname": "string",
          "replyComments": [
            {}
          ]
        }
      ]
    }
  ]
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|id|integer|true|none||none|
|nickname|string|true|none||none|
|content|string|true|none||none|
|avatar|string|true|none||none|
|createTime|string|true|none||none|
|website|string|true|none||none|
|adminComment|boolean|true|none||none|
|parentCommentId|string|true|none||none|
|parentCommentNickname|string|true|none||none|
|replyComments|[[PageCommentVO](#schemapagecommentvo)]|true|none||none|

