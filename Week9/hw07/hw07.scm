(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond
    ((< x 0) -1)
    ((= x 0) 0)
    ((> x 0) 1))
)

(define (square x) (* x x))

(define (pow b n)
  (cond 
    ((= n 0) 1)
    ((even? n) (square (pow b (/ n 2))))
    ((odd? n) (* b (square (pow b (/ (- n 1) 2))))))
)

(define (ordered? s)
  (define (ordered_helper l previous)
    (cond
      ((null? l) True)
      ((< (car l) previous) False)
      (else (ordered_helper (cdr l) (car l)))
    )
  )
  (cond
    ((null? s) True)
    (else (ordered_helper s (car s)))
  )
)

(define (empty? s) (null? s))

(define (add s v)
  (cond
    ((null? s) (cons v nil))
    ((= v (car s)) s)
    ((< v (car s)) (cons v s))
    ((> v (car s)) (cons (car s) (add (cdr s) v)))
  )
)

; Sets as sorted lists
(define (contains? s v)
  (cond
    ((null? s) False)
    ((= (car s) v) True)
    ((> (car s) v) False)
    (else (contains? (cdr s) v))
  )
)

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (intersect s t)
  (cond
    ((null? s) nil)
    ((null? t) nil)
    ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
    ((< (car s) (car t)) (intersect (cdr s) t))
    ((> (car s) (car t)) (intersect s (cdr t)))
  )
)

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
  (cond
    ((null? s) t)
    ((null? t) s)
    ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
    ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
    ((> (car s) (car t)) (cons (car t) (union s (cdr t))))
  )  
)