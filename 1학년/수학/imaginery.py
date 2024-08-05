import matplotlib.pyplot as plt
import numpy as np

# 허수 값 생성: -2에서 2까지 100개의 허수 부분을 생성
imaginary_values = np.linspace(-2, 2, 100)

# 복소수 생성: 실수부는 0, 허수부는 imaginary_values
complex_numbers = 1j * imaginary_values

# 복소수의 제곱 계산
squared_complex_numbers = complex_numbers ** 2

# 그래프 그리기
plt.figure(figsize=(10, 6))

# 실수부와 허수부를 분리
plt.plot(imaginary_values, squared_complex_numbers.real, label='Real part of (ix)^2', color='b')
plt.plot(imaginary_values, squared_complex_numbers.imag, label='Imaginary part of (ix)^2', color='r')

# 그래프 제목 및 라벨 설정
plt.title('Graph of (ix)^2')
plt.xlabel('Imaginary part of x')
plt.ylabel('Value')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# 범례 추가
plt.legend()

# 그래프 보여주기
plt.show()