# 알면 신기한 암호 RSA 알고리즘

## 코드 설명

``` python
def generate_large_prime(bitsize):
    """Generate a large prime number."""
    while True:
        num = random.getrandbits(bitsize)
        if isprime(num):
            return num
```
이 함수는 주어진 비트 크기의 큰 소수를 생성합니다. random.getrandbits(bitsize)를 사용하여
임의의 숫자를 생성하고, sympy의 isprime 함수를 사용하여 그 숫자가 소수인지 확인합니다. 소수일 경우 해당 숫자를 반환합니다.

```python
def generate_keypair(bitsize):
    """Generate RSA key pair (public key, private key)."""
    p = generate_large_prime(bitsize // 2)
    q = generate_large_prime(bitsize // 2)
    n = p * q

    phi = (p - 1) * (q - 1)

    # Choose e
    e = 65537  # A commonly used prime number for e

    # Calculate d
    d = mod_inverse(e, phi)

    return ((e, n), (d, n), (p, q))
```

이 함수는 RSA 키 쌍을 생성합니다:

	•	p와 q는 각각 bitsize // 2 비트 크기의 큰 소수입니다.
	•	n은 두 소수의 곱으로, RSA 모듈러스입니다.
	•	phi는 오일러의 피 함수로, (p - 1) * (q - 1)입니다.
	•	e는 공개 지수로, 일반적으로 65537을 사용합니다.
	•	d는 개인 지수로, mod_inverse(e, phi)를 사용하여 계산합니다.

함수는 공개 키 (e, n), 개인 키 (d, n), 그리고 소수 p와 q를 반환합니다.

```python
def encrypt(public_key, plaintext):
    """Encrypt plaintext using the public key."""
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext
```
이 함수는 주어진 공개 키를 사용하여 평문을 암호화합니다:

	•	plaintext의 각 문자를 ord 함수를 사용하여 아스키 코드 값으로 변환합니다.
	•	각 아스키 코드 값을 e와 n을 사용하여 pow 함수를 통해 암호화합니다.
	•	암호화된 값들을 리스트로 반환합니다.

```python
def decrypt(private_key, ciphertext):
    """Decrypt ciphertext using the private key."""
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext
```

이 함수는 주어진 개인 키를 사용하여 암호문을 복호화합니다:

	•	ciphertext의 각 값을 d와 n을 사용하여 pow 함수를 통해 복호화합니다.
	•	복호화된 아스키 코드 값을 chr 함수를 사용하여 문자로 변환합니다.
	•	복호화된 문자들을 하나의 문자열로 결합하여 반환합니다.


```python
def factorize_n(n):
    """Factorize n into p and q (basic trial division, not efficient for large n)."""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None
```
이 함수는  n 을 소인수분해하여  p 와  q 를 찾습니다:

	•	int(n ** 0.5) + 1까지의 숫자로  n 을 나누어 나누어떨어지는 값이  p 입니다.
	•	나누어떨어지는 값을 찾으면  q 는  n // p 입니다.
	•	이 방법은 단순한 방법으로, 실제 큰  n 에 대해서는 매우 비효율적입니다.




## 소인수분해의 기본 원리

:: 소인수분해란 어떤 정수를 그보다 작은 소수들의 곱으로 표현하는 것을 말합니다. 예를 들어, 15를 소인수분해하면 3과 5가 됩니다. 마찬가지로 RSA에서의 n은 두 큰 소수 p와 q의 곱입니다.

## 소인수분해 알고리즘

:: 소인수분해 알고리즘은 여러 가지가 있지만, 여기서는 가장 단순한 방법인 “trial division”을 사용합니다. 이 방법은  n의 약수를 찾기 위해 작은 수부터 시작하여 루트 n 까지의 모든 수로 나누어 보는 방법입니다.

이유 => 왜  루트 n 까지의 수로만 나누어 보면 되는지 이해하기 위해, 만약  n이 두 수  p 와  q의 곱이라고 가정해봅시다:<br>
```
 n = p * q
 ```
만약  p 와  q 가 모두  루트 n 보다 크다면,  p * q 는  n 보다 커질 것입니다. 따라서, 적어도 하나의 약수는  루트 n  이하에 존재해야 합니다.

### 예제

예를 들어,  n = 35 를 소인수분해해봅시다.

	•	루트 35 ~~ 5.92 이므로 2부터 6까지의 수로 나누어 봅니다.
	•	35는 2로 나누어 떨어지지 않습니다.
	•	35는 3으로 나누어 떨어지지 않습니다.
	•	35는 4로 나누어 떨어지지 않습니다.
	•	35는 5로 나누어 떨어집니다. 따라서  p = 5 이고,  q = 35 // 5 = 7 입니다.


## 중요 코드 설명

```python
def factorize_n(n):
    """Factorize n into p and q (basic trial division, not efficient for large n)."""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None
```

	•	for i in range(2, int(n ** 0.5) + 1): 이 부분은 2부터  루트 n까지의 모든 정수 i에 대해 반복합니다.
	•	int(n ** 0.5) + 1은  n의 제곱근에 1을 더한 값입니다. 제곱근까지의 모든 정수로 나누어 보려는 것입니다.
	•	if n % i == 0: 만약  n이  i로 나누어 떨어지면,  i는  n의 약수입니다.
	•	n % i는  n을  i 로 나눈 나머지입니다. 나머지가 0이면  i 는  n의 약수입니다.
	•	return i, n // i:  i가  n의 약수이면,  p 는  i이고,  q 는  n // i입니다.
	•	n // i는  n 을  i로 나눈 몫으로, 이는  q 를 의미합니다.


## 유클리드 호제법

1. 두 수 중 큰 수를 작은 수로 나눕니다.
2. 나머지가 0이면 작은 수가 최대 공약수가 됩니다.
3. 나머지가 0이 아니면 작은 수가 큰 수가 되고, 나머지를 작은 수로 대체하고 1단계로 돌아갑니다.

ex)
1. 510을 210으로 나눕니다. 나머지는 90입니다. 510 = 210 * 2 + 90
2. 210을 90으로 나눕니다. 나머지는 30입니다. 210 = 90 * 2 + 30
3. 90을 30으로 나눕니다. 나머지는 0입니다. 90 = 30 * 3 + 0
4. 나머지가 0이므로 최대공약수는 30입니다.