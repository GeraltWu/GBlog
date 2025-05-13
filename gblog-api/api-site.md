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

## GET getSite

GET /site

> 返回示例

> 200 Response

```json
{
  "code": 82,
  "msg": "Lorem",
  "data": {
    "siteInfo": {
      "copyright": {
        "title": "细性队点产",
        "siteName": "才科住号"
      }
    },
    "introduction": {
      "avatar": "/img/avatar.jpg",
      "name": "Geralt",
      "github": "https://github.com/GeraltWu",
      "telegram": "amet ea",
      "qq": "ea exercitation tempor eiusmod et",
      "bilibili": "https://space.bilibili.com/350578994?spm_id_from=333.1007.0.0",
      "netease": "ad enim Lorem nulla",
      "email": "wuziran1223@outlook.com",
      "rollText": [
        "aliqua tempor mollit sed"
      ],
      "favorites": [
        {
          "title": "其界工拉去",
          "content": "culpa dolore"
        },
        {
          "title": "那法风电",
          "content": "nulla"
        },
        {
          "title": "越式该值",
          "content": "nisi"
        },
        {
          "title": "有价打路办反",
          "content": "commodo"
        },
        {
          "title": "问全问科联",
          "content": "est veniam elit"
        }
      ]
    },
    "badges": [
      {
        "title": "将风置部",
        "color": "nostrud ut Duis dolor est",
        "value": "consequat ullamco",
        "subject": "cupidatat aliquip irure ex enim",
        "url": "http://gog.mt/zbxmv"
      },
      {
        "title": "部存厂容强",
        "color": "ut mollit voluptate exercitation",
        "value": "commodo fugiat",
        "subject": "incididunt",
        "url": "http://yfhrstrg.re/ipoqpdvoe"
      },
      {
        "title": "变六把认是置去",
        "color": "commodo qui nostrud dolor Duis",
        "value": "et labore",
        "subject": "deserunt magna id in fugiat",
        "url": "http://xspkybfwj.pr/jfjovxza"
      },
      {
        "title": "备展织",
        "color": "qui labore consectetur incididunt est",
        "value": "exercitation tempor ad aliquip",
        "subject": "ea in",
        "url": "http://lfu.mg/maeeeds"
      },
      {
        "title": "今般科养消计",
        "color": "eiusmod exercitation nisi ullamco Lorem",
        "value": "veniam commodo et non",
        "subject": "ipsum Duis sunt laboris proident",
        "url": "http://veblgmba.name/kglo"
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
|» data|object|true|none||none|

# 数据模型

<h2 id="tocS_Tag">Tag</h2>

<a id="schematag"></a>
<a id="schema_Tag"></a>
<a id="tocStag"></a>
<a id="tocstag"></a>

```json
{
  "id": 0,
  "name": "string",
  "color": "string"
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|id|integer|true|none||none|
|name|string|true|none||none|
|color|string|true|none||none|

<h2 id="tocS_Category">Category</h2>

<a id="schemacategory"></a>
<a id="schema_Category"></a>
<a id="tocScategory"></a>
<a id="tocscategory"></a>

```json
{
  "id": 0,
  "name": "string"
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|id|integer|true|none||none|
|name|string|true|none||none|

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

<h2 id="tocS_IntroductionVO">IntroductionVO</h2>

<a id="schemaintroductionvo"></a>
<a id="schema_IntroductionVO"></a>
<a id="tocSintroductionvo"></a>
<a id="tocsintroductionvo"></a>

```json
{
  "avatar": "string",
  "name": "string",
  "github": "string",
  "telegram": "string",
  "qq": "string",
  "bilibili": "string",
  "netease": "string",
  "email": "string",
  "rollText": [
    "string"
  ],
  "favorites": [
    {
      "title": "string",
      "content": "string"
    }
  ]
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|avatar|string|true|none||none|
|name|string|true|none||none|
|github|string|true|none||none|
|telegram|string|true|none||none|
|qq|string|true|none||none|
|bilibili|string|true|none||none|
|netease|string|true|none||none|
|email|string|true|none||none|
|rollText|[string]|true|none||none|
|favorites|[[FavoriteVO](#schemafavoritevo)]|true|none||none|

<h2 id="tocS_FavoriteVO">FavoriteVO</h2>

<a id="schemafavoritevo"></a>
<a id="schema_FavoriteVO"></a>
<a id="tocSfavoritevo"></a>
<a id="tocsfavoritevo"></a>

```json
{
  "title": "string",
  "content": "string"
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|title|string|true|none|最爱名|none|
|content|string|true|none|值|none|

<h2 id="tocS_BadgeVO">BadgeVO</h2>

<a id="schemabadgevo"></a>
<a id="schema_BadgeVO"></a>
<a id="tocSbadgevo"></a>
<a id="tocsbadgevo"></a>

```json
{
  "title": "string",
  "url": "string",
  "subject": "string",
  "value": "string",
  "color": "string"
}

```

### 属性

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|title|string|true|none|徽标完整标题|none|
|url|string|true|none|徽标值的url|none|
|subject|string|true|none|徽标项名|none|
|value|string|true|none|徽标项值|none|
|color|string|true|none|徽标颜色|none|

