import glob
import frontmatter

import qrcode

import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def fix_word(word):
  return "".join([i.lower() for i in word if i.isalpha()])

def get_permalink(title, existing_songs):
  maybe_permalink = "-".join(fix_word(i) for i in title.split())
  if maybe_permalink not in existing_songs:
    return maybe_permalink
  else:
    for i in range(1, 100): # If 100 songs have the same title I give up
      numbered_permalink = maybe_permalink + "-{0}".format(i)
      if numbered_permalink not in existing_songs:
        return numbered_permalink
  assert False

def format_content(text):
  return "<br>\n".join(text.split("\n"))

def make_and_save_qrcode(link_text, file_name):
  img = qrcode.make(link_text)
  img.save("assets/qr-codes/{0}.png".format(file_name))

def write_formatted_file(permalink, post):
  with open("".join(["_formatted_songs/", permalink, ".md"]), 'w') as f:
    f.write(frontmatter.dumps(post))

class Field(object):
  TITLE = "title"
  ARTIST = "artist"

  PERMALINK = "permalink"
  LAYOUT = "layout"

  USER_DEFINED = [TITLE, ARTIST]

defaults = {
  Field.TITLE: "Untitled",
  Field.ARTIST: "Unknown artist"
}

def error(field, filename):
  print("The file {0} needs a {1} in the frontmatter".format(filename,
  field))

def fix_and_write(post, permalink):
  post[Field.LAYOUT] = "song"
  post[Field.PERMALINK] = permalink
  for field in Field.USER_DEFINED:
    if field not in post:
      error(field, song_file)
      post[field] = defaults[field]
  post.content = format_content(post.content)
  write_formatted_file(permalink, post)


def main():

  stream = open("_config.yml", 'r')
  site_config = yaml.load(stream, Loader)
  base_url = site_config["url"]

  # QR code for main page
  make_and_save_qrcode(base_url, "Home")

  permalink_list = []

  for song_file in glob.glob("_songs/*"):
    post = frontmatter.load(song_file)
    permalink = get_permalink(post['title'], permalink_list)
    make_and_save_qrcode(base_url+permalink, permalink)
    fix_and_write(post, permalink)
    permalink_list.append(permalink)


if __name__ == "__main__":
  main()

