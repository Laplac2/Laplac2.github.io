# Google Test

- [断言](#断言)
  - [布尔值检查](#布尔值检查)
  - [数值型数据检查](#数值型数据检查)
  - [字符串检查](#字符串检查)
- [Reference](#reference)

## 断言

gtest 中，断言的宏可以理解为分为两类，一类是 ASSERT 系列，一类是 EXPECT 系列。

1. `ASSERT_*`系列的断言，当检查点失败时，退出当前函数（注意：并非退出当前案例）。
2. `EXPECT_*`系列的断言，当检查点失败时，继续往下执行。

### 布尔值检查

| Fatal assertion          | Nonfatal assertion       | Verifies           |
| ------------------------ | ------------------------ | ------------------ |
| ASSERT_TRUE(condition);  | EXPECT_TRUE(condition);  | condition is true  |
| ASSERT_FALSE(condition); | EXPECT_FALSE(condition); | condition is false |

### 数值型数据检查

| Fatal assertion              | Nonfatal assertion           | Verifies           |
| ---------------------------- | ---------------------------- | ------------------ |
| ASSERT_EQ(expected, actual); | EXPECT_EQ(expected, actual); | expected == actual |
| ASSERT_NE(val1, val2);       | EXPECT_NE(val1, val2);       | val1 != val2       |
| ASSERT_LT(val1, val2);       | EXPECT_LT(val1, val2);       | val1 < val2        |
| ASSERT_LE(val1, val2);       | EXPECT_LE(val1, val2);       | val1 <= val2       |
| ASSERT_GT(val1, val2);       | EXPECT_GT(val1, val2);       | val1 > val2        |
| ASSERT_GE(val1, val2);       | EXPECT_GE(val1, val2);       | val1 >= val2       |

### 字符串检查

| Fatal assertion                             | Nonfatal assertion                          | Verifies                                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------------------- |
| ASSERT_STREQ(expected_str, actual_str);     | EXPECT_STREQ(expected_str, actual_str);     | the two C strings have the same content                 |
| ASSERT_STRNE(str1, str2);                   | EXPECT_STRNE(str1, str2);                   | the two C strings have different content                |
| ASSERT_STRCASEEQ(expected_str, actual_str); | EXPECT_STRCASEEQ(expected_str, actual_str); | the two C strings have the same content, ignoring case  |
| ASSERT_STRCASENE(str1, str2);               | EXPECT_STRCASENE(str1, str2);               | the two C strings have different content, ignoring case |

## gmock

## Reference

1. [googletest source](https://github.com/google/googletest).
2. [googletest-gmock 官方文档](https://github.com/google/googletest/blob/v1.8.x/googlemock/docs/Documentation.md).
3. [玩转 Google 开源 C++单元测试框架 Google Test 系列(gtest)](https://www.cnblogs.com/coderzh/archive/2009/04/06/1426755.html).
4. [googletest-gmock 使用示例](https://zhuanlan.zhihu.com/p/101906555).
