import fire

def myapp(name="World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(myapp)