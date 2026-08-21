#define MAXSIZE 100
#include <stdio.h>
typedef int ElemType;

// 顺序表的定义
typedef struct {
    ElemType data[MAXSIZE];
    int length;
} SqList;

// 初始化顺序表
void initList(SqList *L) {
    L->length = 0;
}

// 在顺序表末尾添加元素
int appendElement(SqList *L, ElemType e) {
    if (L->length >= MAXSIZE) {
        return 0; // 顺序表已满
    }
    L->data[L->length] = e;
    L->length++;
    return 1; // 成功添加元素
}

// 打印顺序表中的元素
void listElements(SqList *L) {
    printf("顺序表中的元素为: ");
    for (int i = 0; i < L->length; i++) {
        printf("%d ", L->data[i]);
    }
    printf("\n");
}

// 在顺序表中插入元素（position为插入位置，不是下标）
int insertElement(SqList *L, int position, ElemType e) {
    if (L->length >= MAXSIZE) {
        return 0; // 顺序表已满
    }

    if (position <= 0 || position > L->length || L->length >= MAXSIZE) {
        return 0; // 插入位置不合法
    }

    for (int i = L->length-1; i >= position-1; i--) {
        L->data[i+1] = L->data[i]; // 元素后移
    }
    L->data[position-1] = e; // 插入新元素
    L->length++; // 更新顺序表长度
    return 1; // 成功插入元素
}

// 删除顺序表中的元素（position为删除位置，不是下标）
int deleteElement(SqList *L, int position) {
    if (L->length == 0) {
        printf("顺序表为空，无法删除元素。\n");
        return 0; // 顺序表为空
    }

    if (position <= 0 || position > L->length) {
        printf("删除位置不合法，无法删除元素。\n");
        return 0; // 删除位置不合法
    }

    for (int i = position-1; i < L->length-1; i++) {
        L->data[i] = L->data[i+1]; // 元素前移
    }
    L->length--; // 更新顺序表长度
    return 1; // 成功删除元素
}

// 查找顺序表中的元素，返回元素位置（从1开始计数），若不存在返回0
int findElement(SqList *L, ElemType e) {
    for (int i = 0; i < L->length; i++) {
        if (L->data[i] == e) {
            return i + 1; // 返回元素位置（从1开始计数）
        }
    }
    return 0; // 元素不存在
}

int main() {
    SqList L;
    initList(&L);
    printf("顺序表初始化完成，当前长度为: %d\n", L.length);
    printf("目前占用的空间为: %d\n", sizeof(L.data));
    
    appendElement(&L, 1);
    appendElement(&L, 2);
    appendElement(&L, 3);
    listElements(&L);

    insertElement(&L, 2, 5);
    listElements(&L);
    deleteElement(&L, 3);
    listElements(&L);

    int pos = findElement(&L, 5);
    if (pos != 0) {
        printf("元素5在顺序表中的位置是: %d\n", pos);
    } else {
        printf("元素5不在顺序表中。\n");
    }

    return 0;
}

// 动态顺序表的定义
typedef struct {
    ElemType *data;
    int length;
}SeqList;
// 初始化动态顺序表
SeqList* initSeqList() {
    SeqList *L = (SeqList *)malloc(sizeof(SeqList));
    L->data = (ElemType *)malloc(MAXSIZE * sizeof(ElemType));
    L->length = 0;
    return L;
}

int main() {
    SeqList *L = initSeqList();
    printf("动态顺序表初始化完成，当前长度为: %d\n", L->length);
    printf("目前占用的空间为: %d\n", sizeof(L->data));
    
    appendElement(L, 1);
    
    // 释放动态顺序表的内存
    free(L->data);
    free(L);
    return 0;
}