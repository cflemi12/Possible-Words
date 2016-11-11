#!/usr/bin/python

import enchant
import itertools

def main():
    while True:
        d = enchant.Dict("en_US")
        try:
            word = raw_input("Enter a word to anagram: ")
            if not d.check(word):
                raise Exception("Must enter valid English word.")
            if len(word.split(' ')) > 1:
                raise Exception("Must enter one word.")
            word = word.strip().lower()
            words = set(''.join(s) for s in itertools.permutations(word))
            print "These are your possible anagrams: "
            for perm in words:
                if d.check(perm):
                    print perm
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            print("\nStopping.")
            break

if __name__ == "__main__":
    main()
