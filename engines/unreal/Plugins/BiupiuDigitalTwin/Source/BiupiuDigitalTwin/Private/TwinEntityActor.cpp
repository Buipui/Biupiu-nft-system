#include "TwinEntityActor.h"

ATwinEntityActor::ATwinEntityActor()
{
    PrimaryActorTick.bCanEverTick = false;
    SchemaVersion = TEXT("biupiu.twin.v1");
    ProvenanceStatus = TEXT("UNVERIFIED");
}
