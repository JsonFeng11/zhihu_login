# zhihu_login
python模拟知乎登录


### 1
 第一步要获取xscf,用requests库获取session,在从session里面获取.
 
### 2
 第二部要获取captcha, 也就是所谓的验证码,获取验证码成功以后就可以获取到完整的data,即可登录成功.
 
 注意:登录多次可能会登录不成功,提示登录次数过多,需要更换ip.本工程是手机号登录,邮箱登录同理.