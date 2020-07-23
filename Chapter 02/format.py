
##  format() 여러 타입을 문자열로 변환 가능
##  {}.format()로 사용
string_a = "{}".format(10)
print(string_a)
print(type(string_a))
print()

format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기 ".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)
print()

##  정수
output_a = "{:d}".format(52)
##  특정 칸에 출력하기
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)
##  빈칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)
print()

## 기호와 함께 출력하기
output_f = "{:+d}".format(52)
output_g = "{:+d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)
print()

##  조합하기
output_j = "{:+5d}".format(52)
output_k = "{:+5d}".format(-52)
output_l = "{:=+5d}".format(52)
output_m = "{:=+5d}".format(-52)
output_n = "{:+=5d}".format(52)
output_o = "{:+=5d}".format(-52)
output_p = "{:+05d}".format(52)
output_q = "{:+05d}".format(-52)

print("# 조합하기")
print(output_j)
print(output_k)
print(output_l)
print(output_m)
print(output_n)
print(output_o)
print(output_p)
print(output_q)
print()

##  부동소수점 출력
output_aa = "{:f}".format(52.273)
output_bb = "{:15f}".format(52.273)
output_cc = "{:+15f}".format(52.273)
output_dd = "{:+015f}".format(52.273)

print("# 부동 소수점 출력")
print(output_aa)
print(output_bb)
print(output_cc)
print(output_dd)
print()

##  소수점 자리수 지정
output_ee = "{:15.3f}".format(52.273)
output_ff = "{:15.2f}".format(52.273)
output_gg = "{:15.1f}".format(52.273)

print("# 소수점 자리수 지정")
print(output_ee)
print(output_ff)
print(output_gg)
print()

##  의미 없는 소수점 제거
output_hh = 52.0
output_ii = "{:g}".format(output_hh)

print("# 의미 없는 소주점 제거")
print(output_hh)
print(output_ii)
print()