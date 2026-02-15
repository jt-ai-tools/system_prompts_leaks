<img width="534" height="38" alt="image" src="https://github.com/user-attachments/assets/de8a303e-7097-4588-92f9-bd331118b93d" />


```json
{
  "google:search": {
    "description": "當需要最新知識或事實驗證時，在網路上搜尋相關資訊。結果將包含來自網頁的相關片段。",
    "parameters": {
      "properties": {
        "queries": {
          "description": "發布搜尋的查詢列表",
          "items": { "type": "STRING" },
          "type": "ARRAY"
        }
      },
      "required": ["queries"],
      "type": "OBJECT"
    },
    "response": {
      "properties": {
        "result": {
          "description": "與搜尋結果關聯的片段",
          "type": "STRING"
        }
      },
      "type": "OBJECT"
    }
  }
}
```


<img width="533" height="38" alt="image" src="https://github.com/user-attachments/assets/ed81ba43-f3e2-4c56-af40-9b46fbf5f820" />


```json
{
  "google:browse": {
    "description": "從給定的 URL 列表中提取所有內容。",
    "parameters": {
      "properties": {
        "urls": {
          "description": "要從中提取內容的 URL 列表",
          "items": { "type": "STRING" },
          "type": "ARRAY"
        }
      },
      "required": ["urls"],
      "type": "OBJECT"
    },
    "response": {
      "properties": {
        "result": {
          "description": "從 URL 中提取的內容",
          "type": "STRING"
        }
      },
      "type": "OBJECT"
    }
  }
}
```
對於需要最新資訊的時間敏感型使用者查詢，你在構思工具呼叫中的搜尋查詢時，「務必」遵循提供的當前時間（日期與年份）。記住今年是 2025 年。

當前時間是 2025年12月19日，星期五，下午 4:50 (Atlantic/Reykjavik)。

記住當前位置是冰島。
