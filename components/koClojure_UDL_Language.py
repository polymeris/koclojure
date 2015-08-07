# Registers the Clojure language in Komodo.

import logging
from koUDLLanguageBase import KoUDLLanguage

log = logging.getLogger("koClojureLanguage")
# log.setLevel(logging.DEBUG)


def registerLanguage(registry):
    log.debug("Registering language Clojure")
    registry.registerLanguage(KoClojureLanguage())


class KoClojureLanguage(KoUDLLanguage):

    # ------------ Komodo Registration Information ------------ #

    name = "Clojure"
    lexresLangName = "Clojure"
    _reg_desc_ = "%s Language" % name
    _reg_contractid_ = "@activestate.com/koLanguage?language=%s;1" % name
    _reg_categories_ = [("komodo-language", name)]
    _reg_clsid_ = "a4d2f79a-b35b-453b-8e3a-d307aa1f3ef4"

    defaultExtension = '.clj'
    primary = 1  # Whether the language shows up in Komodo's first level language menus.

    # ------------ Commenting Controls ------------ #

    commentDelimiterInfo = {
        "line": [';'],     # Lisp-style one line comments
        "block": [],
    }

    # ------------ Indentation Controls ------------ #

    # To support automatic indenting and dedenting after "{([" and "})]"
    supportsSmartIndent = "brace"

    lang_from_udl_family = {'SSL': 'Clojure'}

    searchURL = "https://clojuredocs.org/search?q=%W"

    sample = """; From wikibooks
(defn words [text] (re-seq #"[a-z]+" (.toLowerCase text)))
(defn train [features]
  (reduce (fn [model f] (assoc model f (inc (get model f 1)))) {} features))
(def *nwords* (train (words (slurp "big.txt"))))
"""