from flask import Flask
import webarticle2text
import mechanize
import string
import nltk.data

op = mechanize.Browser()
op.set_handle_robots(False)

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

app = Flask(__name__)

@app.route('/<path:url>')
def article_summary(url):
  r = op.open(url)
  title = op.title()
  raw_html = r.read()
  clean_html = filter(lambda x : x in string.printable,
    raw_html)
  main_text = webarticle2text.extractFromHTML(clean_html)
  sentences = sent_detector.tokenize(main_text)
  # return "<body> <h1>%s</h1> <p><ol><li>%s</li></ol></p></body>" % (
  #  title,
  #  '</li><li>'.join(sentences))
  return "<body> <h1>%s</h1> <p>%s</p></body>" % (
    title,
    ' '.join(sentences))

if __name__ == "__main__":
  app.run(debug=True)
