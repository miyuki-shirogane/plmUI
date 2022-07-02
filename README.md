<!-- TABLE OF CONTENTS -->
<details>
  <summary>目录</summary>
  <ol>
    <li>
      <a href="#项目介绍">项目介绍</a>
      <ul>
        <li><a href="#设计模式">设计模式</a></li>
        <li><a href="#技术选型">技术选型</a></li>
        <li><a href="#实现细节">实现细节</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## 项目介绍

本项目为我司工业互联网SaaS平台中plm项目（产品生命周期）的UI自动化测试项目。采用Python + pytest + Selenium 技术栈完成。

### 设计模式

采用PO设计模式。\
一些原则：
> 1.用公共方法代表UI提供的功能\
> 2.方法应该返回其他PageObject或需要用于断言的数据\
> 3.不暴露页面内部元素给外面\

其核心思想就是封装。只暴露方法，不暴露细节。

### 实现细节

```pageObject```包内含封装的一些页面方法。其中```base_page.py```文件内含一些页面跳转，及监听页面```dialog```数量、获取```alert```信息等公共方法。```debug.py```文件为平常本地调试页面的空间，可以较大限度地节省调试成本。\
```utils```包内含一些工具类：mock数据、读取环境数据等。\
