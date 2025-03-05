<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            font-family: 'Arial', 'Microsoft YaHei', sans-serif;
        }

        .title {
            color: #2c3e50;
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 30px;
        }

        .content {
            line-height: 1.6;
            color: #34495e;
            margin: 20px 0;
        }

        .image-container {
            text-align: center;
            margin: 30px 0;
        }

        .styled-image {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        .highlight {
            color: #e74c3c;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title">{{ title }}</h1>
        
        <p class="content">
            {{ paragraph1 }}
        </p>

        <div class="image-container">
            <img src="{{ image_url }}" alt="描述图片内容" class="styled-image">
        </div>

        <p class="content">
            {{ paragraph2 }}
            <span class="highlight">重点内容</span> 可以这样突出显示
        </p>
    </div>
</body>
</html>