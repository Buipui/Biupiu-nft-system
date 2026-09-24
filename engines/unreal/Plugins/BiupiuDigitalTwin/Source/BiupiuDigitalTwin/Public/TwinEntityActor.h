#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "TwinEntityActor.generated.h"

UCLASS(BlueprintType)
class BIUPIUDIGITALTWIN_API ATwinEntityActor : public AActor
{
    GENERATED_BODY()

public:
    ATwinEntityActor();

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Biupiu|Digital Twin")
    FString EntityId;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Biupiu|Digital Twin")
    FString SchemaVersion;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Biupiu|Digital Twin")
    FString ProvenanceStatus;
};
