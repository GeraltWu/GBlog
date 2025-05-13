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

## GET getArchives

GET /archives

> 返回示例

> 200 Response

```json
{
  "code": 200,
  "msg": "string",
  "data": {
    "totalQuantity": 0,
    "list": [
      {
        "month": "string",
        "list": [
          {
            "id": null,
            "title": null,
            "day": null,
            "password": null,
            "isPrivate": null
          }
        ]
      }
    ]
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
|» data|[ArchiveBlogListVO](#schemaarchivebloglistvo)|true|none||none|
|»» totalQuantity|integer|true|none||none|
|»» list|[[ArchiveBlogMonthlyVO](#schemaarchiveblogmonthlyvo)]|true|none||none|
|»»» month|string|true|none||none|
|»»» list|[[ArchiveBlogVO](#schemaarchiveblogvo)]|true|none||none|
|»»»» id|integer|true|none||none|
|»»»» title|string|true|none||none|
|»»»» day|string|true|none||none|
|»»»» password|string|true|none||none|
|»»»» isPrivate|boolean|true|none||none|

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

<h2 id="tocS_ArchiveBlogVO">ArchiveBlogVO</h2>

<a id="schemaarchiveblogvo"></a>
<a id="schema_ArchiveBlogVO"></a>
<a id="tocSarchiveblogvo"></a>
<a id="tocsarchiveblogvo"></a>

```json
{
  "id": 0,
  "title": "string",
  "day": "string",
  "password": "string",
  "isPrivate": true
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|id|integer|true|none||none|
|title|string|true|none||none|
|day|string|true|none||none|
|password|string|true|none||none|
|isPrivate|boolean|true|none||none|

<h2 id="tocS_ArchiveBlogListVO">ArchiveBlogListVO</h2>

<a id="schemaarchivebloglistvo"></a>
<a id="schema_ArchiveBlogListVO"></a>
<a id="tocSarchivebloglistvo"></a>
<a id="tocsarchivebloglistvo"></a>

```json
{
  "totalQuantity": 0,
  "list": [
    {
      "month": "string",
      "list": [
        {
          "id": 0,
          "title": "string",
          "day": "string",
          "password": "string",
          "isPrivate": true
        }
      ]
    }
  ]
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|totalQuantity|integer|true|none||none|
|list|[[ArchiveBlogMonthlyVO](#schemaarchiveblogmonthlyvo)]|true|none||none|

<h2 id="tocS_ArchiveBlogMonthlyVO">ArchiveBlogMonthlyVO</h2>

<a id="schemaarchiveblogmonthlyvo"></a>
<a id="schema_ArchiveBlogMonthlyVO"></a>
<a id="tocSarchiveblogmonthlyvo"></a>
<a id="tocsarchiveblogmonthlyvo"></a>

```json
{
  "month": "string",
  "list": [
    {
      "id": 0,
      "title": "string",
      "day": "string",
      "password": "string",
      "isPrivate": true
    }
  ]
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|month|string|true|none||none|
|list|[[ArchiveBlogVO](#schemaarchiveblogvo)]|true|none||none|

