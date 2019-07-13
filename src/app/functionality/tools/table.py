from tag import create_tag


def create_table(rows):
	table = create_tag('table', None, {'border': '1px', 'cellpadding': '4px'})
	tbody = create_tag('tbody')
	table.appendChild(tbody)

	for row in rows:
		tr = create_tag('tr')
		tbody.appendChild(tr)
		for cell in row:
			td = create_tag('td', str(cell) if cell else '')
			tr.appendChild(td)

	return table.toprettyxml()
