#include <stdio.h>
#include <stdlib.h>

typedef int ElemType;
// 双向链表存储结构
typedef struct node {
    ElemType data;
    struct node *prev;
    struct node *next;
} Node;

// 初始化双向链表
Node* initDoublyList() {
    Node *head = (Node*)malloc(sizeof(Node));
    head->data = 0;
    head->prev = NULL;
    head->next = NULL;
    return head;
}

// 在双向链表头部插入元素
void insertHead(Node *head, ElemType e) {
    Node *p=(Node*)malloc(sizeof(Node));
    p->data=e;
    p->prev=head;  // 新节点的前驱指向头节点
    p->next=head->next;  // 新节点的后继指向头节点的下一个节点
    if(head->next!=NULL) {  // 如果头节点的下一个节点不为空，则将其前驱指向新节点
        head->next->prev=p;
    }
    head->next=p;  // 头节点的下一个节点指向新节点
}

// 遍历双向链表并打印元素
void listDoublyNode(Node *head) {
    Node *p=head->next;
    while(p!=NULL) {
        printf("%d ",p->data);
        p=p->next;
    }
    printf("\n");
}

// 获取双向链表的尾节点
Node* get_tail(Node *head) {
    Node *p=head;
    while(p->next!=NULL) {
        p=p->next;
    }
    return p;
}

// 在双向链表尾部插入元素
void insertTail(Node *tail, ElemType e) {
    Node *p=(Node*)malloc(sizeof(Node));
    p->data=e;
    p->prev=tail;  // 新节点的前驱指向尾节点
    p->next=NULL;  // 新节点的后继为空
    tail->next=p;  // 尾节点的下一个节点指向新节点
}

// 在指定位置插入元素（position为插入位置，从头指针之后开始计数）
int insertNode(Node *head, int position, ElemType e) {
    Node *p=head->next; // 指向链表的第一个节点
    int i=1;
    // 遍历链表找到插入位置的前一个节点
    while(i<position-1 && p!=NULL) {
        p=p->next;
        i++;
    }
    if(p==NULL) {
        printf("插入位置不合法，无法插入元素。\n");
        return 0; // 插入位置不合法
    }
    // 创建新节点并插入
    Node *newNode=(Node*)malloc(sizeof(Node));
    newNode->data=e;
    newNode->prev=p;  // 新节点的前驱指向插入位置的前一个节点
    newNode->next=p->next;  // 新节点的后继指向插入位置的下一个节点
    if(p->next!=NULL) {
        p->next->prev=newNode;
    }
    p->next=newNode;
    return 1; // 成功插入元素
}

// 删除双向链表中的元素（position为删除位置，从头指针之后开始计数）
int deleteNode(Node *head, int position) {
    Node *p=head->next; // 指向链表的第一个节点
    int i=1;
    // 遍历链表找到删除位置的前一个节点
    while(i<position-1 && p!=NULL) {
        p=p->next;
        i++;
    }
    if(p==NULL) {
        printf("删除位置不合法，无法删除元素。\n");
        return 0; // 删除位置不合法
    }
    // 删除节点
    Node *q=p->next; // 要删除的节点
    if(q==NULL) {
        printf("删除位置不合法，无法删除元素。\n");
        return 0; // 删除位置不合法
    }
    p->next=q->next; // 前一个节点指向要删除节点的下一个节点
    if(q->next!=NULL) {
        q->next->prev=p; // 要删除节点的下一个节点的前驱指向前一个节点
    }
    free(q); // 释放要删除的节点
    return 1; // 成功删除元素
}

int main() {
    Node *head=initDoublyList();
    printf("双向链表初始化完成。\n");
    
    insertHead(head, 1);
    insertHead(head, 2);
    insertHead(head, 3);
    listDoublyNode(head);

    Node *tail=get_tail(head);
    insertTail(tail, 4);
    insertTail(tail, 5);
    listDoublyNode(head);

    insertNode(head, 3, 6);
    listDoublyNode(head);

    deleteNode(head, 4);
    listDoublyNode(head);

    return 0;
}