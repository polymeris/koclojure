(defmacro [param] ; comment
  "Docstring"
  (let [some-text "\n1234\""
        some-char \x
        some-bool true
        some-map  {:lalal "x"}
        some-set  #{:symb0 :zymb1}
        some-regex #"[1-9]"]
   (do  (.javaMethod (JavaCons. (namespace/func 1N 4.5)
                                (otherfunc 2/5 '(1 2 3)
                                                (/ 7.5 0x4)))))
        ~@param
        (nil? nil)
        (>= 0 1))
