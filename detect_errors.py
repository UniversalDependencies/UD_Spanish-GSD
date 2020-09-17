def search_lines_for_errors(filename):
  print(f'Looking for errors in {filename}')
  errors = 0
  with open(filename, 'r') as f:
    for i, line in enumerate(f.readlines()):
      if "�" in line:
        print(f'Error in line {i+1}')
        errors += 1
  if errors == 0:
    print('No errors found!')
  else:
    print(f'{errors} errors were found')

for partition in ['dev', 'test', 'train']:
  filename = f'es_gsd-ud-{partition}.conllu'
  search_lines_for_errors(filename)
  print('='*20)