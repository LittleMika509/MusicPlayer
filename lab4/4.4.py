about_me = (
     "Я хочу спати. Мені 17 років. Намагаюся вчитися новому."
    )


a = about_me.count('а')

for words in about_me.split('. '):
    print(words)

print("Кількість символів 'а':", a)