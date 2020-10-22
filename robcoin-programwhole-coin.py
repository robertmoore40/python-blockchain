import hashlib as hasher
import datetime as date

class Block:
  def __init__(self, index, timestamp, data, previous_hash):