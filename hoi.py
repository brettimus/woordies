from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hoi():
  return 'hoi hoiii!'

@app.route('/words', methods=['GET', 'POST'])
def words():
  words_with_header = []
  with open('SUBTLEX-NL.cd-above2.with-pos.txt') as our_database_lol:
    for entry in our_database_lol:
        # NOTE: our "db" is tab-delimited, so split on a tab
        word = entry.split('\t')[0]
        words_with_header.append(word)
  # Return a list of 1000 words, except for the first (which is the header, and just says "Word")
  words = words_with_header[1:1000]
  # Use a (jinja2) template to render the words list
  return render_template('words.html', words=words)

@app.route('/word/<word>')
def word(word):
  header = []
  word_data = []
  is_header = True
  with open('SUBTLEX-NL.cd-above2.with-pos.txt') as our_database_lol:
    for entry in our_database_lol:
      current_data = entry.split('\t')
      if is_header:
        header = current_data
        is_header = False
      elif current_data[0] == word:
        word_data = current_data
        break
  word_record = dict(zip(header, word_data))
  print(word_record)
  return render_template('word.html', word=word_record)