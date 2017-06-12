## 流程图
```
graph TD
    A(单元测试调用HotelApi.syncRoom) --> B(syncRoom发起任务并保存数据)
    B --> C(RoomSyncRunner执行任务)
    C --> D(捉取酒店产品数据)
    D --> E(将酒店产品转化为HotelRoomProduct)
    E --> B
    B --> A
```
