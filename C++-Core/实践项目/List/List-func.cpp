#include <iostream>
using namespace std;    
struct node
{
int data;
node *next;
};
class CList
{
 node *head;
public:
    CList() {head=NULL;}
    void insert(int adata,int bdata);
    void deletenode(int adata);
    void exchange();
    void outputlist();
    node *gethead() {return head;}  
};

// 输出链表中的元素
void CList::outputlist(){
    node* temp=head;
    while(temp!=NULL){
        cout << temp->data << " ";
        temp=temp->next;
    }
    cout << endl;
}
// 插入结点
void CList::insert(int adata,int bdata){
    //创建新节点
    node* n_node=new node;
    n_node->data=bdata;
    n_node->next=NULL;
    
    if(head==NULL){
        //如果链表为空，则新节点作为头结点
         head=n_node;
    }
    else{
        //先查找，找到数据等于adata的位置
        node* cur=head;
        while(cur->next!=NULL && cur->data!=adata){
            cur=cur->next;
        }
        if(cur->next==NULL){ //如果没有找到，直接插入到链表末尾
            cur->next=n_node;
        }
        else{ //如果找到了，插入到该节点后面
            n_node->next=cur->next;
            cur->next=n_node;
        }
    }
}
//删除节点
void CList::deletenode(int adata){
    if(head==NULL) return; //链表为空，直接返回

    if(head->data==adata){ //如果头结点就是要删除的节点
        node* temp=head;
        head=head->next; //更新头结点
        delete temp; //释放内存
        return;
    }

    node* cur=head;
    while(cur->next!=NULL && cur->next->data!=adata){
        cur=cur->next;
    }
    if(cur->next!=NULL){ //找到了要删除的节点
        node* temp=cur->next;
        cur->next=cur->next->next; //跳过要删除的节点
        delete temp; //释放内存
    }
}
//逆置链表
void CList::exchange(){
    node* cur=head; 
    node* n_head=NULL; //新的头指针

    while(cur){
        cur=head->next;
        head->next=n_head;
        n_head=head;
        head=cur;
    }
    head=n_head; //更新头指针
}

int main()
{
CList L;
int data[10],n,i;
for(i=0;i<10;i++)
cin>>data[i];
L.insert(0,data[0]);
for(i=1;i<10;i++)
   L.insert(0,data[i]);
cin>>n;
L.deletenode(n);
L.outputlist();
L.exchange();
L.outputlist();
return 0;
}