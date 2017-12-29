#!/usr/bin/python

def get_numbers():
  raw_input() # Remove first number
  return [int(x) for x in raw_input().split()]

def get_indices(nums, minimum):
  return [i for i in xrange(len(nums)) if nums[i] == minimum]

def get_minimum_distance(indices):
  minimum = indices[1] - indices[0]
  for i in xrange(1, len(indices)):
    minimum = min(minimum, indices[i] - indices[i-1])
  return minimum

def main():
  nums = get_numbers()
  minimum = min(nums)
  indices = get_indices(nums, minimum)
  print get_minimum_distance(indices)

if __name__ == '__main__':
  main()

