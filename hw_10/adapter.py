class TextAdapter:

    @staticmethod
    def csv_to_html(file_path):
        with open(file_path) as f:
            res = f.readlines()

        header = [k.strip() for k in res[0].split(',')]
        rows = res[1:]
        html_output = ''

        for row in rows:
            row = row.strip().split(',')
            html_output += ''.join(f"<{h}>{r}</{h}>\n" for h, r in zip(header, row))
            html_output += '.' * 35 + '\n'
        return html_output


print(TextAdapter.csv_to_html('team_salary.txt'))
