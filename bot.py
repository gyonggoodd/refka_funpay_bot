from FunPayAPI import Account, Runner, types, enums
import os

TOKEN = os.getenv("GOLDEN_KEY")

acc = Account(TOKEN).get()

runner = Runner(acc)