# Summary

The Spanish UD is converted from the content head version of the [universal
dependency treebank v2.0 (legacy)](https://github.com/ryanmcd/uni-dep-tb).


# Introduction

In addition to converting dependencies from the legacy UD treebank, token level morphology features have been added
automatically using the parsers/taggers in Bohnet et al 2014* and Bohnet et al. 2015** trained on the Ancora***
treebank and converted automatically to UD standards.

Various heuristics have been added to improve the output of the tagger, fix obvious errors and add features that
the tagger did not supply. The changes for v1.2 (November 2015) were done by Miguel Ballesteros, Dan Zeman, and
Héctor Martínez Alonso.

The Spanish UD conforms to the UD guidelines, but there are some exceptions.

* Bohnet, Bernd, et al. "Joint morphological and syntactic analysis for richly inflected languages."
  Transactions of the Association for Computational Linguistics 1 (2013): 415-428.
* Bohnet, Bernd, et al. "Static and Dynamic Feature Selection in Morphosyntactic Analyzers." Under review. 2015.
* Taulé, Mariona, Maria Antònia Martí, and Marta Recasens.
  "AnCora: Multilevel Annotated Corpora for Catalan and Spanish." LREC. 2008.


# Changelog

* 2019-11-15 v2.5
  * Google gave permission to drop the "NC" restriction from the license.
    This applies to the UD annotations (not the underlying content, of which Google claims no ownership or copyright).
* 2019-05-01 v2.4
  * Automatically fixed some auxiliary verbs and copulas.
* 2018-07-01 v2.2
  * Fixed acl-->advcl under VERB ([https://github.com/UniversalDependencies/UD_French-GSD/issues/4](https://github.com/UniversalDependencies/UD_French-GSD/issues/4))
* 2017-03-01 v2.0
  * Converted to UD v2 guidelines.
* 2015-11-15 v1.2
  * Removed duplicite sentences (train overlapped with dev/test, removed from dev/test).
  * Ensured AUX are not heads.
  * Applied type-based POS changes for function words.
  * Changed mwe and name relations to left-headed.
  * Added morphology features (tagger + heuristic rules and semi-automatic fixes).
  * Added lemmas (lemmatizer + heuristic rules).
* 2015-05-15 v1.1
  * Second release.
* 2015-01-15 v1.0
  * First release. No lemmas, no features. Dependencies converted from the legacy UD treebank.



```
===================================
Universal Dependency Treebanks v2.0
(legacy information)
===================================

=========================
Licenses and terms-of-use
=========================

For the following languages

  German, Spanish, French, Indonesian, Italian, Japanese, Korean and Brazilian
  Portuguese

we will distinguish between two portions of the data.

1. The underlying text for sentences that were annotated. This data Google
   asserts no ownership over and no copyright over. Some or all of these
   sentences may be copyrighted in some jurisdictions.  Where copyrighted,
   Google collected these sentences under exceptions to copyright or implied
   license rights.  GOOGLE MAKES THEM AVAILABLE TO YOU 'AS IS', WITHOUT ANY
   WARRANTY OF ANY KIND, WHETHER EXPRESS OR IMPLIED.

2. The annotations -- part-of-speech tags and dependency annotations. These are
   made available under a CC BY-SA 4.0. GOOGLE MAKES
   THEM AVAILABLE TO YOU 'AS IS', WITHOUT ANY WARRANTY OF ANY KIND, WHETHER
   EXPRESS OR IMPLIED. See attached LICENSE file for the text of CC BY-NC-SA.

Portions of the German data were sampled from the CoNLL 2006 Tiger Treebank
data. Hans Uszkoreit graciously gave permission to use the underlying
sentences in this data as part of this release.

Any use of the data should reference the above plus:

  Universal Dependency Annotation for Multilingual Parsing
  Ryan McDonald, Joakim Nivre, Yvonne Quirmbach-Brundage, Yoav Goldberg,
  Dipanjan Das, Kuzman Ganchev, Keith Hall, Slav Petrov, Hao Zhang,
  Oscar Tackstrom, Claudia Bedini, Nuria Bertomeu Castello and Jungmee Lee
  Proceedings of ACL 2013

=======
Contact
=======

ryanmcd@google.com
joakim.nivre@lingfil.uu.se
slav@google.com
See https://github.com/ryanmcd/uni-dep-tb for more details
```


=== Machine-readable metadata =================================================
Data available since: UD v1.0
License: CC BY-SA 4.0
Includes text: yes
Genre: blog news reviews wiki
Lemmas: automatic
UPOS: converted from manual
XPOS: not available
Features: automatic
Relations: converted from manual
Contributors: Ballesteros, Miguel; Martínez Alonso, Héctor; McDonald, Ryan; Pascual, Elena; Silveira, Natalia; Zeman, Daniel; Nivre, Joakim
Contributing: here
Contact: zeman@ufal.mff.cuni.cz
===============================================================================
(Original treebank contributors: Quirmbach-Brundage, Yvonne; LaMontagne, Adam; Souček, Milan; Järvinen, Timo; Radici, Alessandra)
