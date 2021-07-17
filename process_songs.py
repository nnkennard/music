import glob
import frontmatter

import qrcode

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

def main():

  formatted_songs = {}

  for song_file in glob.glob("_songs/*"):
    post = frontmatter.load(song_file)
    permalink = get_permalink(post['title'], formatted_songs)
    post['permalink'] = permalink
    img = qrcode.make("localhost:4000/"+permalink)
    img.save("qr-codes/{0}.png".format(permalink))

    post['layout'] = 'song'
    post.content = format_content(post.content)
    formatted_songs[permalink] = post
    with open("".join(["_formatted_songs/", permalink, ".md"]), 'w') as f:
      f.write(frontmatter.dumps(post))


if __name__ == "__main__":
  main()

