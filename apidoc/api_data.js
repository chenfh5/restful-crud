define({ "api": [
  {
    "type": "delete",
    "url": "v3/personlevel/names/:name/phones/:phone/ages/:age",
    "title": "删除实例",
    "group": "PersonLevelSet",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "names",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "ages",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "参数样例:",
          "content": "{\n    \"name\": \"r1\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "成功返回:",
          "content": "{\n    \"message\": \"bkdata\",\n    \"code\": \"79\",\n    \"data\": \"destroy 1 records\",\n    \"result\": true\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rdemo/rdemo/views.py",
    "groupTitle": "PersonLevelSet",
    "name": "DeleteV3PersonlevelNamesNamePhonesPhoneAgesAge"
  },
  {
    "type": "get",
    "url": "v3/personlevel/names/:name/phones/:phone/ages/:age",
    "title": "获取单个实例详情",
    "group": "PersonLevelSet",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "names",
            "description": "<p>None</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": "<p>None</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "ages",
            "description": "<p>0</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "成功返回:",
          "content": "{\n    \"message\": \"bkdata\",\n    \"code\": \"78\",\n    \"data\": [\n        {\n            \"description\": \"\",\n            \"created_at\": \"2018-10-23T13:18:06.265000Z\",\n            \"updated_at\": \"2018-10-23T13:18:06.265000Z\",\n            \"created_by\": \"\",\n            \"name\": \"r2\",\n            \"phone\": \"13800138000\",\n            \"address\": \"深圳\",\n            \"age\": 23,\n            \"id\": 36,\n            \"updated_by\": \"\"\n        },\n        {\n            \"description\": \"\",\n            \"created_at\": \"2018-10-23T13:22:40.437000Z\",\n            \"updated_at\": \"2018-10-23T13:22:40.437000Z\",\n            \"created_by\": \"\",\n            \"name\": \"qqqq\",\n            \"phone\": \"13800138000\",\n            \"address\": \"us\",\n            \"age\": 45,\n            \"id\": 38,\n            \"updated_by\": \"\"\n        }\n    ],\n    \"result\": true\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rdemo/rdemo/views.py",
    "groupTitle": "PersonLevelSet",
    "name": "GetV3PersonlevelNamesNamePhonesPhoneAgesAge"
  },
  {
    "type": "post",
    "url": "v3/personlevel/names/:name/phones/:phone/ages",
    "title": "新增实例",
    "group": "PersonLevelSet",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "names",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phones",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "ages",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "参数样例:",
          "content": "{\n    \"name\": \"placeholder for serializer\",\n    \"phone\": \"12345678912\",\n    \"age\": 45,\n    \"address\": \"us\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "成功返回:",
          "content": "{\n    \"message\": \"bkdata\",\n    \"code\": \"79\",\n    \"data\": {\n        \"name\": \"qqqq\",\n        \"age\": 45,\n        \"address\": \"us\",\n        \"created_by\": \"\",\n        \"phone\": \"13800138000\",\n        \"updated_by\": \"\",\n        \"id\": 38,\n        \"description\": \"\"\n    },\n    \"result\": true\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rdemo/rdemo/views.py",
    "groupTitle": "PersonLevelSet",
    "name": "PostV3PersonlevelNamesNamePhonesPhoneAges"
  },
  {
    "type": "put",
    "url": "v3/personlevel/names/:name/phones/:phone/ages/:age",
    "title": "替换实例内容",
    "group": "PersonLevelSet",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "names",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "ages",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "参数样例:",
          "content": "{\n    \"name\": \"placeholder for serializer\",\n    \"phone\": \"12345678912\",\n    \"age\": 99,\n    \"address\": \"中国\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "成功返回:",
          "content": "{\n    \"message\": \"bkdata\",\n    \"code\": \"79\",\n    \"data\": {\n        \"name\": \"qqqq\",\n        \"age\": 99,\n        \"address\": \"中国\",\n        \"created_by\": \"\",\n        \"phone\": \"13800138000\",\n        \"updated_by\": \"\",\n        \"id\": 38,\n        \"description\": \"\"\n    },\n    \"result\": true\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rdemo/rdemo/views.py",
    "groupTitle": "PersonLevelSet",
    "name": "PutV3PersonlevelNamesNamePhonesPhoneAgesAge"
  },
  {
    "type": "delete",
    "url": "/personrest/99?age=2",
    "title": "获取单个实例详情",
    "group": "PersonRESTSet",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "name",
            "description": "<p>optional</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "phone",
            "description": "<p>optional</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "age",
            "description": "<p>optional</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>optional</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数样例:",
          "content": "{\n    \"name\": \"c1\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "成功返回:",
          "content": "{\n    \"message\": \"bkdata\",\n    \"code\": \"89\",\n    \"data\": \"destroy 1 records\",\n    \"result\": true\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rdemo/rdemo/views.py",
    "groupTitle": "PersonRESTSet",
    "name": "DeletePersonrest99Age2"
  },
  {
    "type": "get",
    "url": "/personrest/99?age=2",
    "title": "获取单个实例详情",
    "group": "PersonRESTSet",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "name",
            "description": "<p>optional</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "phone",
            "description": "<p>optional</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "age",
            "description": "<p>optional</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>optional</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "成功返回:",
          "content": "{\n    \"message\": \"bkdata\",\n    \"code\": \"88\",\n    \"data\": [\n        {\n            \"description\": \"\",\n            \"created_at\": \"2018-10-23T13:08:24.732000Z\",\n            \"updated_at\": \"2018-10-23T13:08:24.732000Z\",\n            \"created_by\": \"\",\n            \"name\": \"r1\",\n            \"phone\": \"13800138000\",\n            \"address\": \"cn\",\n            \"age\": 23,\n            \"id\": 35,\n            \"updated_by\": \"\"\n        },\n        {\n            \"description\": \"\",\n            \"created_at\": \"2018-10-23T13:18:06.265000Z\",\n            \"updated_at\": \"2018-10-23T13:18:06.265000Z\",\n            \"created_by\": \"\",\n            \"name\": \"r2\",\n            \"phone\": \"13800138000\",\n            \"address\": \"深圳\",\n            \"age\": 23,\n            \"id\": 36,\n            \"updated_by\": \"\"\n        }\n    ],\n    \"result\": true\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rdemo/rdemo/views.py",
    "groupTitle": "PersonRESTSet",
    "name": "GetPersonrest99Age2"
  },
  {
    "type": "post",
    "url": "/personrest",
    "title": "新增实例",
    "group": "PersonRESTSet",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "age",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "address",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "参数样例:",
          "content": "{\n    \"name\": \"c1\",\n    \"phone\": \"13800138000\",\n    \"age\": \"23\",\n    \"address\": \"深圳\",\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "成功返回:",
          "content": "{\n    \"message\": \"bkdata\",\n    \"code\": \"89\",\n    \"data\": {\n        \"name\": \"r1\",\n        \"age\": 23,\n        \"address\": \"深圳\",\n        \"created_by\": \"\",\n        \"phone\": \"13800138000\",\n        \"updated_by\": \"\",\n        \"id\": 35,\n        \"description\": \"\"\n    },\n    \"result\": true\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rdemo/rdemo/views.py",
    "groupTitle": "PersonRESTSet",
    "name": "PostPersonrest"
  },
  {
    "type": "put",
    "url": "/personrest/99?age=2",
    "title": "获取单个实例详情",
    "group": "PersonRESTSet",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "age",
            "description": "<p>optional</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>optional</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数样例:",
          "content": "{\n    \"name\": \"c1\",\n    \"phone\": \"13800138000\",\n    \"age\": \"23\",\n    \"address\": \"深圳\",\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "成功返回:",
          "content": "{\n    \"message\": \"bkdata\",\n    \"code\": \"89\",\n    \"data\": {\n        \"name\": \"r1\",\n        \"age\": 34,\n        \"address\": \"cn\",\n        \"created_by\": \"\",\n        \"phone\": \"13800138000\",\n        \"updated_by\": \"\",\n        \"id\": 35,\n        \"description\": \"\"\n    },\n    \"result\": true\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rdemo/rdemo/views.py",
    "groupTitle": "PersonRESTSet",
    "name": "PutPersonrest99Age2"
  },
  {
    "type": "get",
    "url": "/person/create1/?name=xxx&phone=xxx&age=11&address=cn",
    "title": "新增实例",
    "group": "PersonSet",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "age",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "address",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "参数样例:",
          "content": "{\n    \"name\": \"c1\",\n    \"phone\": \"13800138000\",\n    \"age\": \"23\",\n    \"address\": \"深圳\",\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "成功返回:",
          "content": "{\n    \"name\": \"c1\",\n    \"age\": \"11\",\n    \"address\": \"深圳\",\n    \"created_by\": \"\",\n    \"phone\": \"13800138000\",\n    \"updated_by\": \"\",\n    \"id\": 34,\n    \"description\": \"\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rdemo/rdemo/views.py",
    "groupTitle": "PersonSet",
    "name": "GetPersonCreate1NameXxxPhoneXxxAge11AddressCn"
  },
  {
    "type": "get",
    "url": "/person/retrieve1/?name=xxx&phone=xxx&age=11&address=xxx",
    "title": "获取单个实例详情",
    "group": "PersonSet",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "name",
            "description": "<p>optional</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "phone",
            "description": "<p>optional</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "age",
            "description": "<p>optional</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>optional</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "成功返回:",
          "content": "{\n    \"0\": {\n        \"name\": \"qq\",\n        \"age\": 99,\n        \"address\": \"中国\",\n        \"created_by\": \"\",\n        \"phone\": \"13800138000\",\n        \"updated_by\": \"\",\n        \"id\": 31,\n        \"description\": \"\"\n    },\n    \"1\": {\n        \"name\": \"qqqq\",\n        \"age\": 45,\n        \"address\": \"us\",\n        \"created_by\": \"\",\n        \"phone\": \"13800138000\",\n        \"updated_by\": \"\",\n        \"id\": 33,\n        \"description\": \"\"\n    },\n    \"2\": {\n        \"name\": \"c1\",\n        \"age\": 11,\n        \"address\": \"cn\",\n        \"created_by\": \"\",\n        \"phone\": \"13800138000\",\n        \"updated_by\": \"\",\n        \"id\": 34,\n        \"description\": \"\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rdemo/rdemo/views.py",
    "groupTitle": "PersonSet",
    "name": "GetPersonRetrieve1NameXxxPhoneXxxAge11AddressXxx"
  },
  {
    "type": "get",
    "url": "/person/update1/?name=xxx&phone=xxx&age=11&address=xxx",
    "title": "删除实例",
    "group": "PersonSet",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "name",
            "description": "<p>optional</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "phone",
            "description": "<p>optional</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "age",
            "description": "<p>optional</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>optional</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "成功返回:",
          "content": "\"destroy 3 records\"",
          "type": "String"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rdemo/rdemo/views.py",
    "groupTitle": "PersonSet",
    "name": "GetPersonUpdate1NameXxxPhoneXxxAge11AddressXxx"
  },
  {
    "type": "get",
    "url": "/person/update1/?name=xxx&phone=xxx&age=11&address=xxx",
    "title": "替换实例内容",
    "group": "PersonSet",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": ""
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "age",
            "description": "<p>optional</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "address",
            "description": "<p>optional</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数样例:",
          "content": "{\n    \"name\": \"c1\",\n    \"phone\": \"13800138000\",\n    \"age\": \"23\",\n    \"address\": \"深圳\",\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "成功返回:",
          "content": "{\n    \"name\": \"c1\",\n    \"age\": \"11\",\n    \"address\": \"深圳\",\n    \"created_by\": \"\",\n    \"phone\": \"13800138000\",\n    \"updated_by\": \"\",\n    \"id\": 34,\n    \"description\": \"\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "rdemo/rdemo/views.py",
    "groupTitle": "PersonSet",
    "name": "GetPersonUpdate1NameXxxPhoneXxxAge11AddressXxx"
  }
] });
