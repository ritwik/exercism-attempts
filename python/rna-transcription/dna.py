#!/usr/bin/python
# coding=UTF-8

class DNA(object):

  def __init__(self, dna_string):

    self.dna_string = dna_string

  def to_rna(self):

    return self.dna_string.replace("T", "U")
