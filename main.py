import cx_Oracle
# running stored procedures


def main():
    try:
        print(f'The current install client version software: {cx_Oracle.clientversion()}')
        connection = cx_Oracle.connect("sys", "password", "STRPT", mode=cx_Oracle.SYSDBA, encoding="UTF-8")
        #print(f'Current connection client DB version software: {str(connection.version())}')
        cur = connection.cursor()
        outvar =cur.var(int)
        returnvar = cur.callproc("RPTDBA.MAK_LOAD_PRE_DONOR", [])
        # returnvar = cur.callproc("RPTDBA.MAK_LOAD_DONOR", [])

        print(f"finished running load donor exit code: {returnvar}")

    except connection.DatabaseError as exc:
        err, = exc.args
        print("Oracle-Error-Code:", err.code)
        print("Oracle-Error-Message:", err.message)
    finally:
        connection.close()



if __name__ == '__main__':
    main()
