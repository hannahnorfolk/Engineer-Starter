from dotenv import load_dotenv
import os
#os is operating system, we need this to see another file in its directory

load_dotenv()

print(os.getenv('secret'))
#getting an environment variable 