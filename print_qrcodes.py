import glob
import frontmatter

HTML_TEMPLATE = """
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<link rel="stylesheet" href="assets/css/printme.css">
</head>
<body>
<p class='text-center' style='font-size:72px'> Song Index:  </p>
<img class='center' src='assets/qr-codes/Home.png' style='width:300px'/>
<br>
<br>
<div class ='container'>
<div class='row'>
<div class='col-md-6 offset-md-3'>
<table class="table" style='width:60%'>
{0}
</table>
</div>
</div>
</div>
</body>
</html>
"""

IMAGE_CELL = "<td><img src='assets/qr-codes/{0}.png' style='width:150px'/></td>"
TEXT_CELL = "<td><br/><h2>{0}</h2><br/><p style='font-size:20px'><i>{1}</i></p></td>"
def table_builder(rows):
  table_builder = ""
  for row in rows:
    title, artist, permalink = row
    table_builder += "<tr>"
    table_builder += TEXT_CELL.format(title, artist)
    table_builder += IMAGE_CELL.format(permalink)
    table_builder += "</tr>\n"

  return HTML_TEMPLATE.format(table_builder)

def main():
  rows = []
  for formatted_song_file in glob.glob("_formatted_songs/*"):
    post = frontmatter.load(formatted_song_file)
    rows.append(tuple(post[x] for x in "title artist permalink".split()))

  with open("printme.html" ,'w') as f:
    f.write(table_builder(sorted(rows)))


if __name__ == "__main__":
  main()

