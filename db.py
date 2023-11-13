import mysql.connector


def conexao_db():
    db = mysql.connector.connect(
        host='localhost',
        user = 'snake_game',
        password = 'snakegame321',
        database = 'snake_game'
    )

    return db


con = conexao_db()

def get_list_usuarios():
    sql = " select nome_usua, pont_usua, date_format(data_jogd, '%d/%m/%Y') data_jogd from usuario order by pont_usua desc "

    cursor = con.cursor()

    cursor.execute(sql)

    resultado = cursor.fetchall()

    return resultado


def cadastra_usua(nome_usua, pont_usua):
    sql = '''
        insert into usuario (
            nome_usua, 
            pont_usua, 
            data_jogd
        ) values (
            %s, 
            %s, 
            sysdate()
        )'''

    cursor = con.cursor()

    cursor.execute(sql, [nome_usua, pont_usua])

    con.commit()