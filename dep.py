import mysql.connector as my

def recherche(requete, serv, utilisateur, mdp, base):
    """fonction permetant de ce connecter en securité et de demander une requette a notre base de donnée"""
    assert requete != str, 'la requette doit etre du texte'
    conn = my.connect (
        host = serv,
        user = utilisateur,
        password = mdp,
        database = base,
    )
    cursor = conn.cursor()
    cursor.execute(requete)
    resultats = cursor.fetchall()
    cursor.close
    conn.close
    return resultats
