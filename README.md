## 流程图
```
graph TD
    A(单元测试发起任务)-->B(HotelSyncRunner)
    B-->C(捉取接口酒店数据)
    C-->D(将接口酒店数据转换为HotelMapping)
    D-->B
    B-->A
```
