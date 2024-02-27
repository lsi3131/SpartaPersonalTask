import sys
import getpass


# ----- 코드 정의 ------
class Member:
    def __init__(self, name='', username='', password=''):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f'id={self.username}, name={self.name}')


class Post:
    def __init__(self, title='', content='', author=''):
        self.title = title
        self.content = content
        self.author = author


def create_post(member: Member, title, content):
    return Post(title, content, member.username)


g_members = [
    Member(name='lee', username='id1', password='passwd1'),
    Member(name='kim', username='id2', password='passwd2'),
    Member(name='jang', username='id3', password='passwd3'),
]

g_posts = [
    create_post(g_members[0], 'Dodgers', 'Bellinger to miss start of season after shoulder surgery'),
    create_post(g_members[0], 'Yankees', '(\'No need\' to talk contract extension'),
    create_post(g_members[0], 'Angels', 'Ohtani to start season as two-way player'),
    create_post(g_members[1], 'Mets', 'he\'s good to go after shoulder scare'),
    create_post(g_members[1], 'Braves', 'he\'s \'100 percent\' after knee surgery'),
    create_post(g_members[1], 'Red Sox', 'Correa say they\'re \'all in\' for 2023 season'),
    create_post(g_members[2], 'Cubs', 'Cubs\' Bryant says he\'s \'excited\' for fresh start with Rockies'),
    create_post(g_members[2], 'Phillies', 'We\'re going to win the NL East'),
    create_post(g_members[2], 'Giants', 'announces retirement after 12 seasons'),
]


def print_members(members):
    print('====print members====')
    for member in members:
        member.display()


def print_post_title_by_member(username: str):
    print(f'====print post title(id={username})====')
    posts_in_member = [post for post in g_posts if post.author == username]
    for post in posts_in_member:
        print(post.title)


def print_post_title_by_word_in_content(word: str):
    print(f'====print post title(word={word})====')
    posts = [post for post in g_posts if word in post.content]
    for post in posts:
        print(post.title)


def print_all():
    print_members(g_members)

    print_post_title_by_member(g_members[1].username)
    print_post_title_by_member(g_members[0].username)
    print_post_title_by_member(g_members[2].username)

    print_post_title_by_word_in_content('go')
    print_post_title_by_word_in_content('Ohtani')


# =========================  심화 학습  ==================================

g_registered_member_table: [str, Member] = {
}

g_registered_post_list: [Post] = []


def print_registered_member():
    print('[등록된 유저 리스트]')
    for key in list(g_registered_member_table):
        g_registered_member_table[key].display()


def print_registered_post():
    print('[등록된 게시물 리스트]')
    for post in g_registered_post_list:
        print(f'작성자ID={post.author}, 제목={post.title}, 내용={post.content}')


def create_member_loop():
    while True:
        username = input('ID를 입력하세요: ')
        if len(username) == 0:
            continue
        if username in g_registered_member_table:
            print(f'id(={username})는 이미 존재합니다.')
            continue
        break

    while True:
        password1 = getpass.getpass("비밀번호를 입력하세요: ")
        if len(password1) == 0:
            continue
        password2 = getpass.getpass("비밀번호를 다시 한번 입력하세요: ")
        if password1 != password2:
            print(f'비밀번호가 다릅니다. 비밀번호를 다시 한번 입력하세요.')
            continue
        break

    while True:
        name = input('회원 이름을 입력하세요: ')
        if len(name) == 0:
            continue
        break
    message = f'회원으로 등록되었습니다. ID : {username}, 이름 : {name} '
    print(message)

    g_registered_member_table[username] = Member(name=name, username=username, password=password1)


def create_post_loop():
    while True:
        username = input('작성자 ID를 입력하세요(돌아가기: !q, ID조회: !pm): ')
        if username == '!q':
            return
        if username == '!pm':
            print_registered_member()
            continue

        if username not in g_registered_member_table:
            print(f'작성자 id(={username})가 존재하지 않습니다.')
            continue
        break

    while True:
        title = input("제목을 입력하세요: ")
        if len(title) == 0:
            continue

        break

    while True:
        content = input("내용을 입력하세요: ")
        if len(content) == 0:
            continue

        break

    message = f'게시글이 등록되었습니다. 작성자ID : {username}, 제목 : {title} '
    print(message)

    g_registered_post_list.append(Post(title=title, content=content, author=username))


g_command_table = {
    'pm': [print_registered_member, '등록된 유저 출력'],
    'pp': [print_registered_post, '등록된 게시물 출력'],
    'cm': [create_member_loop, '멤버 생성'],
    'cp': [create_post_loop, '게시물 생성'],
    'q': [exit, '종료']
}


def create_input_message():
    input_message = '명령에 해당하는 키를 입력하세요('
    for key in g_command_table:
        comment = g_command_table[key][1]
        input_message += f'{comment}:{key}, '
    input_message = input_message[:-2] + '): '
    return input_message


def command_loop():
    while True:
        command_key = input(create_input_message())
        if command_key not in g_command_table:
            continue

        g_command_table[command_key][0]()


if __name__ == '__main__':
    # 기본 과제
    # print_all()

    # 추가 과제
    command_loop()
