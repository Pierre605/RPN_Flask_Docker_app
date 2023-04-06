import os

cmd_query = '''curl -X POST "http://127.0.0.1:5000/" -H "Content-Type: application/x-www-form-urlencoded" --data-urlencode '''
cmd_export = '''curl -X POST "http://127.0.0.1:5000/export/" -H "Content-Type: application/x-www-form-urlencoded" --data-urlencode "export=executeExportCSV" > PNI_calaculations_report.csv'''
cmd_clear_history = '''curl -X POST "http://127.0.0.1:5000/delete/" -H "Content-Type: application/x-www-form-urlencoded" --data-urlencode "clear=deleteDB"'''


def query_api_by_cli():
    prompt_query = input("Your PNI syntaxed calculation query: ")
    query = f'''"query={prompt_query}"'''
    return os.system(cmd_query + str(query))

def export_by_cli():
    return os.system(cmd_export)

def clear_by_cli():
    return os.system(cmd_clear_history)


while True:
    prompt_action = input("PNI calcul query ('q'), Export result list ('e'), Clear result list ('c'): ")

    if prompt_action == "q":
        query_api_by_cli()
        print('\n')
        break
    elif prompt_action == "e":
        export_by_cli()
        print('\n')
        break
    elif prompt_action == "c":
        clear_by_cli()
        print('\n')
        break
