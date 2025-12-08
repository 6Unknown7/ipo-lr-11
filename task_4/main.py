# Задание 4: Создаём HTML страницу с новостями
# Простейший вариант для новичка

print("=" * 50)
print("ЗАДАНИЕ 4: Создаём HTML страницу")
print("=" * 50)

# Читаем данные из файла (или создаём примерные)
print("\n📖 Читаем данные о новостях...")

# Примерные данные (если файла нет)
данные = [
    {"номер": 1, "заголовок": "Hacker News is great", "комментарии": 234},
    {"номер": 2, "заголовок": "Python 3.12 Released", "комментарии": 15},
    {"номер": 3, "заголовок": "Understanding AI Models", "комментарии": 4},
    {"номер": 4, "заголовок": "Learn Programming", "комментарии": 42},
]

print(f"📊 Найдено {len(данные)} новостей")

print("\n🎨 Создаём красивую HTML страницу...")

# Создаём HTML файл
html_код = """
<!DOCTYPE html>
<html>
<head>
    <title>Новости Hacker News</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            padding: 20px;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        .comments {
            background-color: #2196F3;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            display: inline-block;
        }
        .link {
            text-align: center;
            margin-top: 20px;
        }
        a {
            color: #4CAF50;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📰 Новости Hacker News</h1>
        
        <table>
            <tr>
                <th>№</th>
                <th>Заголовок</th>
                <th>Комментарии</th>
            </tr>
"""

# Добавляем строки с новостями
for новость in данные:
    html_код += f"""
            <tr>
                <td>{новость['номер']}</td>
                <td>{новость['заголовок']}</td>
                <td><span class="comments">💬 {новость['комментарии']}</span></td>
            </tr>
"""

# Завершаем HTML
html_код += """
        </table>
        
        <div class="link">
            <p>Источник данных: <a href="https://news.ycombinator.com/" target="_blank">Hacker News</a></p>
        </div>
    </div>
</body>
</html>
"""

# Сохраняем в файл
try:
    with open("index.html", "w", encoding="utf-8") as файл:
        файл.write(html_код)
    
    print("✅ Файл index.html успешно создан!")
    print("\n📂 Что создано:")
    print("1. Файл index.html - красивая веб-страница")
    print("2. Страница с заголовком")
    print("3. Страница с фоном")
    print("4. Таблица с новостями")
    print("5. Ссылка на источник")
    
    print("\n👉 Откройте файл index.html в браузере!")
    
except Exception as e:
    print(f"❌ Ошибка: {e}")