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

def get_usua_list():
    sql = '''
           select id_usua,
                  nome_usua,
                  pont_usua,
                  date_format(data_jogd, '%d/%m/%Y') data_jogd 
             from usuario
           '''

    cursor = con.cursor()

    cursor.execute(sql)

    rslt = cursor.fetchall()

    for x in rslt:
        print(x)


def cadastra_usua(nome_usua):
    sql = 'insert into usuario (nome_usua) values (%s)'

    cursor = con.cursor()

    vlr = nome_usua

    cursor.execute(sql, vlr)

    con.commit()


def atualiza_pont(id_usua, pont):
    sql = f'''
        update usuario set 
            pont_usua = {pont}, 
            data_jogd = sysdate()
        where id_usua = {id_usua}
    '''


cadastra_usua(['lallaslas'])

