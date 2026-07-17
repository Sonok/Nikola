# Pattern 2 — Parsing / Stack (Days 3–4)

Known Tesla favorite (firmware/diagnostics parsing flavor). One template covers all four
calculator-family questions. Do them in this order — each builds on the last.

## 20. Valid Parentheses (Easy) — warmup
```python
def isValid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    st = []
    for c in s:
        if c in pairs:
            if not st or st.pop() != pairs[c]:
                return False
        else:
            st.append(c)
    return not st
```

## 150. Evaluate Reverse Polish Notation (Medium)
Stack of ints; on operator, pop b then a (ORDER MATTERS for - and /).
Python gotcha they watch for: truncate toward zero → `int(a / b)`, NOT `a // b`
(`-3 // 2 == -2` but the answer wants -1).

## 227. Basic Calculator II (Medium) — the one that actually gets asked
`+ - * /`, no parens. Template: current number + last operator + stack of signed terms.
```python
def calculate(s):
    st, num, op = [], 0, '+'
    for i, c in enumerate(s):
        if c.isdigit():
            num = num * 10 + int(c)
        if c in '+-*/' or i == len(s) - 1:   # flush on operator or end
            if op == '+': st.append(num)
            elif op == '-': st.append(-num)
            elif op == '*': st.append(st.pop() * num)
            else: st.append(int(st.pop() / num))   # truncate toward zero
            op, num = c, 0
    return sum(st)
```
Why it works: * and / bind immediately to the previous term; + and - defer to the final sum.
Spaces are skipped naturally (they're neither digit nor operator... except the last-char flush —
note `i == len(s)-1` handles a trailing digit; trailing spaces also hit the flush harmlessly).

## 224. Basic Calculator I (Hard-ish Medium)
`+ - ( )`. Running result + sign; on `(` push (result, sign) and reset; on `)` pop and combine.
```python
def calculate(s):
    st, res, sign, num = [], 0, 1, 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c in '+-':
            res += sign * num
            sign, num = (1 if c == '+' else -1), 0
        elif c == '(':
            st.append((res, sign))
            res, sign = 0, 1
        elif c == ')':
            res += sign * num
            prev, psign = st.pop()
            res, num = prev + psign * res, 0
    return res + sign * num
```
Follow-up they like: "now combine I and II" (parens AND precedence) — recursive descent; be
ready to sketch the approach verbally even if not code it.

## 393. UTF-8 Validation (Medium)
Bit manipulation on the leading byte: count leading 1s → that's the byte-length (0 → 1 byte;
1 alone → invalid; >4 → invalid); the next (count-1) bytes must start `10`.
`(byte >> 5) == 0b110` → 2 bytes, `>> 4 == 0b1110` → 3, `>> 3 == 0b11110` → 4,
continuation check: `(byte >> 6) == 0b10`. Very Tesla-flavored: validating a byte protocol.
