#include "../include/biupiu_visual_render_graph.h"
#include <cstdint>
static int req(bool v,int n){return v?0:n;}
int main(){
 biupiu_render_graph_id g=0;if(int r=req(biupiu_render_graph_create(&g)==0&&g!=0,1))return r;
 biupiu_render_pass_id a=0,b=0,c=0; biupiu_render_pass_desc pd{BIUPIU_PASS_GPU,1,1,2};
 if(int r=req(biupiu_render_graph_add_pass(g,&pd,&a)==0,2))return r; pd.priority=2;
 if(int r=req(biupiu_render_graph_add_pass(g,&pd,&b)==0,3))return r; pd.kind=BIUPIU_PASS_CPU;pd.priority=3;
 if(int r=req(biupiu_render_graph_add_pass(g,&pd,&c)==0,4))return r;
 if(int r=req(biupiu_render_graph_add_dependency(g,a,b)==0,5))return r;
 if(int r=req(biupiu_render_graph_add_dependency(g,b,c)==0,6))return r;
 if(int r=req(biupiu_render_graph_compile(g)==0,7))return r;
 uint64_t h1=0,h2=0;if(int r=req(biupiu_render_graph_execute(g,7,&h1)==0&&h1!=0,8))return r;
 if(int r=req(biupiu_render_graph_execute(g,7,&h2)==0&&h1==h2,9))return r;
 biupiu_render_graph_info info{};if(int r=req(biupiu_render_graph_get_info(g,&info)==0&&info.pass_count==3&&info.dependency_count==2,10))return r;
 if(int r=req(biupiu_render_graph_destroy(g)==0&&biupiu_render_graph_destroy(g)!=0,11))return r;
 return 0;
}