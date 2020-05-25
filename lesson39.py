from Parser_class import Parser
# print('Напишите никнейм пользователя')
# site = input()
# site = 'https://lichess.org/@/' + site
site = 'https://lichess.org/@/MrUltraBulletChess'
print('Человек с ником MrUltraBulletChess сейчас')
global flag
while True:
    parser = Parser(site, 'news.txt')
    parser.run()
# print(parser.html)
# print(parser.results)